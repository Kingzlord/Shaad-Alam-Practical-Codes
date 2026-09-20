const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const message = document.getElementById("message");
const levelMenu = document.getElementById("levelMenu");
const level1Btn = document.getElementById("level1Btn");
const level2Btn = document.getElementById("level2Btn");

const keys = {};

let currentLevel = "tutorial";
let gameWon = false;
let tutorialCompleted = false;
let showedLightWarning = false;

const player = {
  x: 50,
  y: 250,
  radius: 12,
  speed: 3
};

let playerStart = { x: 50, y: 250 };
let exit = {};
let walls = [];
let lights = [];

const levels = {
  tutorial: {
    playerStart: { x: 50, y: 250 },
    exit: { x: 730, y: 220, width: 40, height: 60 },
    walls: [
      { x: 250, y: 0, width: 20, height: 300 },
      { x: 500, y: 200, width: 20, height: 300 }
    ],
    lights: [
      {
        x: 360,
        y: 180,
        radius: 65,
        speed: 1.5,
        minX: 330,
        maxX: 470,
        direction: 1
      }
    ]
  },

  level1: {
    playerStart: { x: 50, y: 250 },
    exit: { x: 730, y: 50, width: 40, height: 60 },
    walls: [
      { x: 180, y: 100, width: 20, height: 400 },
      { x: 350, y: 0, width: 20, height: 300 },
      { x: 550, y: 200, width: 20, height: 300 }
    ],
    lights: [
      {
        x: 280,
        y: 80,
        radius: 60,
        speed: 2,
        minX: 240,
        maxX: 420,
        direction: 1
      },
      {
        x: 650,
        y: 350,
        radius: 70,
        speed: 2,
        minX: 580,
        maxX: 730,
        direction: -1
      }
    ]
  },

  level2: {
    playerStart: { x: 60, y: 440 },
    exit: { x: 700, y: 40, width: 50, height: 60 },
    walls: [
      { x: 150, y: 0, width: 20, height: 280 },
      { x: 320, y: 220, width: 20, height: 280 },
      { x: 500, y: 0, width: 20, height: 280 },
      { x: 650, y: 220, width: 20, height: 280 }
    ],
    lights: [
      {
        x: 220,
        y: 340,
        radius: 55,
        speed: 1.8,
        minX: 180,
        maxX: 320,
        direction: 1
      },
      {
        x: 430,
        y: 120,
        radius: 65,
        speed: 1.4,
        minX: 380,
        maxX: 520,
        direction: -1
      },
      {
        x: 700,
        y: 320,
        radius: 60,
        speed: 2.2,
        minX: 620,
        maxX: 740,
        direction: 1
      }
    ]
  }
};

document.addEventListener("keydown", (e) => {
  keys[e.key.toLowerCase()] = true;
});

document.addEventListener("keyup", (e) => {
  keys[e.key.toLowerCase()] = false;
});

function loadLevel(levelName) {
  currentLevel = levelName;
  const level = levels[levelName];

  playerStart = { ...level.playerStart };
  player.x = playerStart.x;
  player.y = playerStart.y;

  exit = { ...level.exit };
  walls = level.walls.map(w => ({ ...w }));
  lights = level.lights.map(l => ({ ...l }));

  gameWon = false;
  showedLightWarning = false;
  levelMenu.style.display = "none";

  if (levelName === "tutorial") {
    message.textContent = "Move with WASD";
  } else {
    message.textContent = "";
  }
}

window.loadLevel = loadLevel;

function resetPlayer() {
  player.x = playerStart.x;
  player.y = playerStart.y;
  gameWon = false;

  if (currentLevel === "tutorial") {
    message.textContent = "Move with WASD";
  }

  alert("You walked into lights");
}

function circleRectCollision(cx, cy, radius, rx, ry, rw, rh) {
  const closestX = Math.max(rx, Math.min(cx, rx + rw));
  const closestY = Math.max(ry, Math.min(cy, ry + rh));

  const dx = cx - closestX;
  const dy = cy - closestY;

  return dx * dx + dy * dy < radius * radius;
}

function movePlayer() {
  if (gameWon || levelMenu.style.display === "block") return;

  let dx = 0;
  let dy = 0;

  if (keys["w"] || keys["arrowup"]) dy -= player.speed;
  if (keys["s"] || keys["arrowdown"]) dy += player.speed;
  if (keys["a"] || keys["arrowleft"]) dx -= player.speed;
  if (keys["d"] || keys["arrowright"]) dx += player.speed;

  let newX = player.x + dx;
  let newY = player.y + dy;

  newX = Math.max(player.radius, Math.min(canvas.width - player.radius, newX));
  newY = Math.max(player.radius, Math.min(canvas.height - player.radius, newY));

  let blocked = false;
  for (const wall of walls) {
    if (circleRectCollision(newX, newY, player.radius, wall.x, wall.y, wall.width, wall.height)) {
      blocked = true;
      break;
    }
  }

  if (!blocked) {
    player.x = newX;
    player.y = newY;
  }
}

function updateLights() {
  for (const light of lights) {
    light.x += light.speed * light.direction;

    if (light.x > light.maxX || light.x < light.minX) {
      light.direction *= -1;
    }
  }
}

function checkTutorialHints() {
  if (currentLevel !== "tutorial") return;
  if (showedLightWarning) return;

  const light = lights[0];
  const dx = player.x - light.x;
  const dy = player.y - light.y;
  const distance = Math.sqrt(dx * dx + dy * dy);

  if (distance < light.radius + 100) {
    message.textContent = "Watch out for lights";
    showedLightWarning = true;
  }
}

function checkLightCollision() {
  for (const light of lights) {
    const dx = player.x - light.x;
    const dy = player.y - light.y;
    const distance = Math.sqrt(dx * dx + dy * dy);

    if (distance < player.radius + light.radius) {
      resetPlayer();
      return;
    }
  }
}

function checkWin() {
  const touchingExit =
    player.x + player.radius > exit.x &&
    player.x - player.radius < exit.x + exit.width &&
    player.y + player.radius > exit.y &&
    player.y - player.radius < exit.y + exit.height;

  if (!touchingExit) return;

  gameWon = true;

  if (currentLevel === "tutorial") {
    tutorialCompleted = true;
    level1Btn.disabled = false;
    level2Btn.disabled = false;
    message.textContent = "Tutorial complete!";
    levelMenu.style.display = "block";
  } else {
    message.textContent = `${currentLevel} complete!`;
    levelMenu.style.display = "block";
  }
}

function drawBackground() {
  ctx.fillStyle = "#111";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function drawExit() {
  ctx.fillStyle = "#2ecc71";
  ctx.fillRect(exit.x, exit.y, exit.width, exit.height);

  ctx.fillStyle = "#0b2";
  ctx.font = "16px Arial";
  ctx.fillText("EXIT", exit.x + 3, exit.y - 8);
}

function drawWalls() {
  ctx.fillStyle = "#444";
  for (const wall of walls) {
    ctx.fillRect(wall.x, wall.y, wall.width, wall.height);
  }
}

function drawLights() {
  for (const light of lights) {
    const gradient = ctx.createRadialGradient(
      light.x, light.y, 10,
      light.x, light.y, light.radius
    );
    gradient.addColorStop(0, "rgba(255, 255, 180, 0.9)");
    gradient.addColorStop(1, "rgba(255, 255, 180, 0.05)");

    ctx.beginPath();
    ctx.arc(light.x, light.y, light.radius, 0, Math.PI * 2);
    ctx.fillStyle = gradient;
    ctx.fill();
  }
}

function drawPlayer() {
  ctx.beginPath();
  ctx.arc(player.x, player.y, player.radius, 0, Math.PI * 2);
  ctx.fillStyle = "#000";
  ctx.fill();
  ctx.strokeStyle = "#777";
  ctx.stroke();
}

function gameLoop() {
  drawBackground();
  movePlayer();
  updateLights();
  checkTutorialHints();
  checkLightCollision();
  checkWin();

  drawExit();
  drawWalls();
  drawLights();
  drawPlayer();

  requestAnimationFrame(gameLoop);
}

loadLevel("tutorial");
gameLoop();