import { Component, useState } from "react";
import ReactDOM from "react-dom";
// import { App } from "./App";

function Test(props) {
  const [text, setText] = useState("<empty>")
  fetch(`${props.serverUrl}/hello`)
    .then(response => response.json())
    .then(data => setText(data.join(' ')))
    .catch(error => {console.error('Fetch failed:',error)})
  return <h1>{text}</h1>
}

function App(props) {
  return <Test serverUrl="http://localhost:8000" />
}

const app = document.getElementById("app");
ReactDOM.render(<App />, app);