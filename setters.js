// let halley = {
//     _name: 'Halley',
//     _behavior: 0,
   
//     set name(newname) {
//       return this._name=newname;
//     },
   
//     set behavior() {
//       return this._behavior;
//     },
   
//     incrementBehavior() {
//       this._behavior++;
//     }
//   }
// halley.name="Lucky"
// console.log(halley._name)

class Dog {
    constructor(name) {
      this._name = name;
      this._behavior = 0;
    }
  
    get name() {
      return this._name;
    }
    get behavior() {
      return this._behavior;
    }   
  
    incrementBehavior() {
      this._behavior ++;
    }
  }
  
  const halley = new Dog('Halley');
  console.log(halley.name); // Print name value to console
  console.log(halley.behavior); // Print behavior value to console
  halley.incrementBehavior(); // Add one to behavior
  console.log(halley.name); // Print name value to console
  console.log(halley.behavior); // Print behavior value to console
  