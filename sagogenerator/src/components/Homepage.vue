<template>
  <div class="hello">
    <h1 style="text-align: center; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 40px;">Välkommen till SagoGeneratorn!</h1>
    <hr style="border: 1px solid red;">
    <p style="text-align: center; margin: 20px; font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif; font-size: 20px;"><i>SagoGeneratorn</i> är ett projekt där AI används för att hitta på nya sagor och historier på svenska
    <br/>För att själv använda tjänsten, skriv bara i en titel i fältet nedan, klicka på knappen, och se vilken historia du får tillbaka. Lycka till!
    </p>    
    <p style="font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; font-size: 12px;">Sagorna som genereras är inte garanterat relaterade till den titel du valt. Ibland ger den tillbaka en helt egen historia, med annan inspiration. Då kan du antingen skicka ännu en förfrågan, eller använda svaret du fått, då det kan vara ganska komiskt.</p>
    <div style="margin-top: 45px">
      <input type="text" v-model="title">
      <button @click="submit" :disabled="title.length === 0">Skicka</button>
    </div>
    <div class="textbox">
      <!-- Här kommer texten som genererats! -->
      <h1 class="title">{{showTitle}}</h1>
      <p class="text">{{text}}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Homepage',
  data: () => ({
    title: "Den stora dagen",
    showTitle: "",
    text: ""
  }),
  methods: {
    submit() {
      console.log("Getting text...")
      let title = this.title + "."
      this.showTitle = this.title
      this.text = "Var god vänta i några sekunder..."

      axios.get('http://127.0.0.1:5000/text?title='+ title)
      .then(response => {
        this.text = response.data.text
      })
      .catch(e => {
        console.log(e)
        this.showTitle = "FEL!"
        this.text = "Ett fel har inträffat, var god vänta och försök igen!"  
      })

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.title{
  font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  font-size: 20pt;
}
.text{
  font-family: Georgia, 'Times New Roman', Times, serif;
  font-size: 14pt;
  text-align: justify;
  margin-left: 10px;
  margin-right: 10px;
}
.textbox {
  border: 3px dotted red;
  background-color: wheat;
  width: 60%;
  left: 50%; 
  position: absolute; 
  margin-top: 2.5%; 
  margin-right: -50%; 
  transform: translate(-50%, 0%);
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
button {
  background-color: red;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
button:hover {
  background-color: rgb(141, 0, 0);
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  display: inline-block;
  font-size: 16px;
}
button:disabled {
  background-color: rgb(255, 157, 157);
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
input {
  height: 36px; 
  padding: 12px 20px;
  box-sizing: border-box;
  transition: 0.5s;
  outline: none;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
  font-size: 16px;
  margin: 5px; 
  display: inline-block;
  border: 3px solid #ccc;
}
input:focus {
  border: 3px solid red;
}
</style>
