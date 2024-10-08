Candy.Preloader = function(game){
	// define width and height of the game
	Candy.GAME_WIDTH = 640;
	Candy.GAME_HEIGHT = 960;
};
Candy.Preloader.prototype = {
	preload: function(){
		// set background color and preload image
		this.stage.backgroundColor = '#B4D9E7';
		this.preloadBar = this.add.sprite((Candy.GAME_WIDTH-311)/2, (Candy.GAME_HEIGHT-27)/2, 'preloaderBar');
		this.load.setPreloadSprite(this.preloadBar);
		// load images
		this.load.image('background', 'static/Monster_Wants_Candy/img/background.png');
		this.load.image('floor', 'static/Monster_Wants_Candy/img/floor.png');
		this.load.image('monster-cover', 'static/Monster_Wants_Candy/img/monster-cover.png');
		this.load.image('title', 'static/Monster_Wants_Candy/img/title.png');
		this.load.image('game-over', 'static/Monster_Wants_Candy/img/gameover.png');
		this.load.image('score-bg', 'static/Monster_Wants_Candy/img/score-bg.png');
		this.load.image('button-pause', 'static/Monster_Wants_Candy/img/button-pause.png');
		// load spritesheets
		this.load.spritesheet('candy', 'static/Monster_Wants_Candy/img/candy.png', 82, 98);
		this.load.spritesheet('monster-idle', 'static/Monster_Wants_Candy/img/monster-idle.png', 103, 131);
		this.load.spritesheet('button-start', 'static/Monster_Wants_Candy/img/button-start.png', 401, 143);
	},
	create: function(){
		// start the MainMenu state
		this.state.start('MainMenu');
	}
};