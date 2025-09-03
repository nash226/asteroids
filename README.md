Asteroids (Python & Pygame)

A Python implementation of the classic **Asteroids** arcade game, built using [Pygame](https://www.pygame.org/). 

Guide your spaceship, blast asteroids, and survive as long as you can!

---

Features

- Player-controlled spaceship with rotation and thrust

- Asteroids that split apart when destroyed

- Collision detection between ship, bullets, and asteroids

---

Requirements

- Python **3.10+**

- [Pygame](https://www.pygame.org/)

---

Setup

Clone this repository and install dependencies:

```bash

git clone https://github.com/nash226/asteroids.git

cd asteroids

pip install pygame

---

Controls

w / d — Rotate ship

⬆️ — Thrust forward

Spacebar — Shoot

close window — Quit game

---

Project Structure

src
├── main.py           # Entry point and game loop
├── player.py         # Player spaceship logic
├── asteroid.py       # Asteroid behavior
├── shot.py           # Player shots logic
├── circleshape.py    # Base class for circular entities
|__ constants.py      # Game constants and settings

<video controls src="Screen Recording 2025-09-03 at 3.19.05 AM.mov" title="Title"></video>

