const meshCanvas = document.getElementById('meshCanvas');
const ctx = meshCanvas.getContext('2d');

let meshNodes = [];
const nodeCount = 80; // Adjust for density
const connectionDistance = 250; // How close nodes must be to connect
const nodeSpeed = 0.3; // Keep it slow for a "background" feel

// Resize meshCanvas to fill window
function resize() {
  meshCanvas.width = window.innerWidth;
  meshCanvas.height = window.innerHeight;
}

window.addEventListener('resize', resize);
resize();

// Node Object
class MeshNode {
  constructor() {
    this.x = Math.random() * meshCanvas.width;
    this.y = Math.random() * meshCanvas.height;
    this.vx = (Math.random() - 0.5) * nodeSpeed;
    this.vy = (Math.random() - 0.5) * nodeSpeed;
    this.radius = 4;
  }

  update() {
    this.x += this.vx;
    this.y += this.vy;

    // Bounce off edges
    if (this.x < 0 || this.x > meshCanvas.width) this.vx *= -1;
    if (this.y < 0 || this.y > meshCanvas.height) this.vy *= -1;
  }

  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
    ctx.fillStyle = 'rgba(100, 150, 200, 0.3)'; // Subtle blue/grey
    ctx.fill();
  }
}

// Create initial nodes
for (let i = 0; i < nodeCount; i++) {
  meshNodes.push(new MeshNode());
}

function animate() {
  ctx.clearRect(0, 0, meshCanvas.width, meshCanvas.height);

  for (let i = 0; i < meshNodes.length; i++) {
    meshNodes[i].update();
    meshNodes[i].draw();

    // Check distances to draw connections
    for (let j = i + 1; j < meshNodes.length; j++) {
      const dx = meshNodes[i].x - meshNodes[j].x;
      const dy = meshNodes[i].y - meshNodes[j].y;
      const distance = Math.sqrt(dx * dx + dy * dy);

      if (distance < connectionDistance) {
        // Opacity fades as they move apart (the "disconnecting" effect)
        const opacity = 1 - (distance / connectionDistance);
        ctx.beginPath();
        ctx.moveTo(meshNodes[i].x, meshNodes[i].y);
        ctx.lineTo(meshNodes[j].x, meshNodes[j].y);
        ctx.strokeStyle = `rgba(150, 150, 150, ${opacity * 0.3})`; 
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    }
  }
  requestAnimationFrame(animate);
}

animate();