let team = {

    _players: [
    {
    firstName: 'Pablo',
    lastName: 'Sanchez',
    age: 11
    },
    {
    firstName: 'Pablo2',
    lastName: 'Sanchez2',
    age: 22
    },
    {
    firstName: 'Pablo3',
    lastName: 'Sanchez3',
    age: 33
    }
  
    ],
    _games: [
    {
    opponent: 'Broncos',
    teamPoints: 42,
    opponentPoints: 27
    },///////////////
    {
    opponent: 'Broncos2',
    teamPoints: 22,
    opponentPoints: 11
    },//////////////
    {
    opponent: 'Broncos3',
    teamPoints: 55,
    opponentPoints: 66
    }
    
    ],///////////
    get players() {
         return this._players;
    },
    get games() {
         return this._games;
    },
  
    addPlayer(firstName, lastName, age) {
    let player = {
        firstName: firstName,
        lastName: lastName,
        age: age
      };
        this.players.push(player);
    },
  
    addGame(oppName, points, oppPoints) {
    let game = {
        oppName: oppName,
        points: points,
        oppPoints: oppPoints
      }
        this.games.push(game);
    }
    
  };
  
  
  team.addPlayer("A","B",99);
  team.addPlayer("C","B",89);
  team.addPlayer("F","B",79);
  
  console.log(team.players);
  
  team.addGame("aa",100,50);
  team.addGame("a2a",300,220);
  team.addGame("a3a",200,10);
  team.addGame("a3a",500,530);
  
  console.log(team.games);
  
  
  
  
  
  
  
  