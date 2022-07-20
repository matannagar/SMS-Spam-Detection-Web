import React, { useState, useEffect } from 'react';
import axios from 'axios';

import Button from "./components/Button";
import Header from "./components/Header";
import Introduction from './components/Introduction';
import Textbox from "./components/Textbox";
import Prediction from "./components/Prediction"
import Credits from "./components/Credits"

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");
  const [color, setColor] = useState("green")

  var bodyFormData = new FormData();
  bodyFormData.append('sms', query)

  const classify = async function () {
    await axios.post(`http://127.0.0.1:5000/predict`, bodyFormData)
      .then(res => {
        let classification;
        if (res.data[0][0]['label'] === 'LABEL_0') {
          classification = 'Non-Spam :)';
          setColor('green')
        } else {
          classification = 'Spam :(';
          setColor('red');
        }
        setResult(classification);
        setQuery("")
      })
      .catch((error) => {
        console.log(error);
      })
  }

  return (
    <div className="App">
      <div className="container">
        <Header />
        <Introduction />
        <Textbox query={query} setQuery={setQuery} setResult={setResult} />

        {(query !== '') ? <Button classify={classify} /> : ''}
        <Prediction result={result} color={color} />
      </div>
    </div>
  );
}

export default App;
