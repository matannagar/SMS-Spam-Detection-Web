import React, { useState, useEffect } from 'react';
import axios from 'axios';

import Button from "./components/Button";
import Header from "./components/Header";
import Textbox from "./components/Textbox";
import Prediction from "./components/Prediction"
import Credits from "./components/Credits"

function App() {
  const [query, setQuery] = useState("");
  const [result, setResult] = useState("");

  const classify = function () {

    var bodyFormData = new FormData();
    bodyFormData.append('sms', query)

    axios.post(`http://127.0.0.1:5000/predict`, bodyFormData)
      .then(res => {
        const classification = (res.data[0][0]['label'] === 'LABEL_0') ? 'Non-Spam' : 'Spam';
        setResult(classification);
        setQuery("")
      })
      .catch((error) => {
        console.log(error);
      })
  }

  return (
    <div className="App">
      <Header />
      <Textbox query={query} setQuery={setQuery} />

      {(query !== '') ? <Button classify={classify} /> : ''}
      <Prediction result={result} />
    </div>
  );
}

export default App;
