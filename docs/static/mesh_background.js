const canvas = document.getElementById('meshCanvas');
const ctx = canvas.getContext('2d');

let nodes = [];
const nodeCount = 80; // Adjust for density
const connectionDistance = 150; // How close nodes must be to connect
const nodeSpeed = 0.2; // Keep it slow for a "background" feel

// Resize canvas to fill window
function resize() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

window.addEventListener('resize', resize);
resize();

// Node Object
class Node {
  constructor() {
    this.x = Math.random() * canvas.width;
    this.y = Math.random() * canvas.height;
    this.vx = (Math.random() - 0.5) * nodeSpeed;
    this.vy = (Math.random() - 0.5) * nodeSpeed;
    this.radius = 4;
  }

  update() {
    this.x += this.vx;
    this.y += this.vy;

    // Bounce off edges
    if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
    if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
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
  nodes.push(new Node());
}

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let i = 0; i < nodes.length; i++) {
    nodes[i].update();
    nodes[i].draw();

    // Check distances to draw connections
    for (let j = i + 1; j < nodes.length; j++) {
      const dx = nodes[i].x - nodes[j].x;
      const dy = nodes[i].y - nodes[j].y;
      const distance = Math.sqrt(dx * dx + dy * dy);

      if (distance < connectionDistance) {
        // Opacity fades as they move apart (the "disconnecting" effect)
        const opacity = 1 - (distance / connectionDistance);
        ctx.beginPath();
        ctx.moveTo(nodes[i].x, nodes[i].y);
        ctx.lineTo(nodes[j].x, nodes[j].y);
        ctx.strokeStyle = `rgba(150, 150, 150, ${opacity * 0.3})`; 
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    }
  }
  requestAnimationFrame(animate);
}

animate();