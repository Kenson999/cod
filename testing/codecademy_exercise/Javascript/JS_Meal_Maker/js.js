const menu = {
  _courses: {
  appetizers: [],
  mains: [],
  desserts: [],
  },

  
  set appetizers(appetizers) {
  this._courses.appetizers = appetizers
  },

  set mains(mains) {
  this._courses.mains = mains
  },

  set desserts(desserts) {
  this._courses.desserts = desserts
  },
  
  get courses() {
  return {
      courses: this._courses.courses
  }
  },

  get appetizers() {
  return {
      appetizers: this._courses.appetizers
  }
  },

  get mains() {
  return {
      mains: this._courses.mains
  }
  },
  

  get desserts() {
  return {
      desserts: this._courses.desserts
  };
  }

  addDishToCourse(courseName, dishName, dishPrice) {
  const dush = {
  name: dishName,
  dishPrice: dishPrice,
  };
}

    this._courses[courseName].push(dish);
  },
  getRandomDishFromCourse(courseName) {
    const dishes = this._courses[courseName];
    const randomIndex = Math.floor(Math.random() * dishes.length);
    return[randomIndex];
  },
  generateRandomMeal() {
    const appetizers = this.getRandomDishFromCourse('appetizers');
    const mains = this.getRandomDishFromCourse('mains');
    const dessert = this.getRandomDishFromCourse('dessert');
    const totalPrice = appetizer.price = main.price + dessert.price;
    return `Your meal is ${appetizer.name}, ${main.name}, and ${dessert.name},
    and the total price is ${totalPrice}`;
  }
  };

menu.addDishToCourse('appetizer', 'aa', 1);
menu.addDishToCourse('appetizer', 'bb', 2);
menu.addDishToCourse('appetizer', 'cc', 3);

menu.addDishToCourse('mains', 'dd', 4);
menu.addDishToCourse('mains', 'ee', 5);
menu.addDishToCourse('mains', 'ff', 6);

menu.addDishToCourse('desserts', 'gg', 7);
menu.addDishToCourse('desserts', 'hh', 8);
menu.addDishToCourse('desserts', 'ii', 9);

const meal = menu.generateRandomMeal();
console.log(meal);
//https://www.youtube.com/watch?v=dfQlhjmb-P0&ab_channel=Codecademy
