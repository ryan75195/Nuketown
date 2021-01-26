# Nuketown AI
Python implimentation of the classic black ops map nuketown. This project plans to redesign this game in a 2d structure with all game behaviour. Then, testing various AI models, have two AI agents play against eachother. The end goal is to connect this via xrpc and connect to one of the bots on xbox to play aginst the AI on the original game.

Game UI & Gameplay
<img align="left" src="https://github.com/ryan75195/Nuketown/blob/master/Gameplay.png">
    <style type="text/css">
    .image-left {
      display: block;
      margin-left: auto;
      margin-right: auto;
      float: right;
    }
    </style>

Navigation Grid(Nodes) for AI traversal. Network is generated dynamically and ensures the agent avoids collisions with walls & illegal areas.

<img align="left" src="https://github.com/ryan75195/Nuketown/blob/master/Nodes.png">
    <style type="text/css">
    .image-left {
      display: block;
      margin-left: auto;
      margin-right: auto;
      float: right;
    }
    </style>
