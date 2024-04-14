/*********************************************************/
/***** Written By: SATYAKI DE                        *****/
/***** Written On: 10-Apr-2024                       *****/
/***** Updated On: 14-Apr-2024                       *****/
/*****                                               *****/
/***** Objective: This is the main react app, which  *****/
/***** will interact with the Flask-API that feds    *****/
/***** all the outputs of LLM Evaluation KPIs based  *****/
/***** on the supplied inputs.                       *****/
/*********************************************************/

import React, { useState } from 'react';
import './App.css';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

function App() {
  const initialInputs = {
    question: '',
    context: '',
    personaResponse: '',
    guideline: '',
    groundTruth: '',
    evaluationMethod: ''
  };

  const [inputs, setInputs] = useState(initialInputs);
  const [results, setResults] = useState({});
  const [submitted, setSubmitted] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setInputs(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async () => {
    setIsLoading(true);
    const response = await fetch('http://localhost:5000/evaluate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(inputs)
    });
    const data = await response.json();
    setResults(data);
    setInputs(initialInputs);  // Clear inputs after submission
    setIsLoading(false);
    setSubmitted(true);
  };

  const chartData = {
    labels: Object.keys(results).filter(key => key.includes('Score')),
    datasets: [
      {
        label: 'Evaluation Scores',
        data: Object.keys(results).filter(key => key.includes('Score')).map(key => results[key]),
        backgroundColor: [
          'rgba(54, 162, 235, 0.5)',
          'rgba(255, 99, 132, 0.5)',
          'rgba(255, 206, 86, 0.5)',
          'rgba(75, 192, 192, 0.5)',
          'rgba(153, 102, 255, 0.5)',
          'rgba(255, 159, 64, 0.5)'
        ],
        borderColor: [
          'rgba(54, 162, 235, 1)',
          'rgba(255, 99, 132, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1
      }
    ],
  };

  const chartOptions = {
    scales: {
      y: {
        beginAtZero: true,
        max: 1
      }
    },
    maintainAspectRatio: false
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Evaluation App</h1>
      </header>
      <div className="input-section">
        {Object.keys(inputs).map((inputKey) => (
          <div key={inputKey} style={{ width: '50%' }}>
            <input
              type="text"
              name={inputKey}
              placeholder={`Enter ${inputKey.replace(/([A-Z])/g, ' $1').trim()}`}
              value={inputs[inputKey]}
              onChange={handleInputChange}
              style={{ width: '90%', margin: '10px', padding: '10px' }}
            />
          </div>
        ))}
        <div style={{ width: '100%', display: 'flex', justifyContent: 'center' }}>
          <button onClick={handleSubmit}>Evaluate</button>
        </div>
      </div>
      {isLoading && (
        <div className="loading-container">
          <img src="/Wheel.jpg" alt=" " /> {/* Make sure the image is placed in the public directory */}
          <p>Our Agent is working on your request. Just Hang Tight! :)</p>
        </div>
      )}
      {!isLoading && submitted && (
        <>
          <div className="chart-container" style={{ height: '400px', width: '80%', margin: '20px auto' }}>
            <Bar data={chartData} options={chartOptions} />
          </div>
          <div className="text-section" style={{ display: 'flex', justifyContent: 'space-around', width: '100%' }}>
            <div className="column">
              {Object.entries(results).filter(([key, _]) => key.includes('Explanation')).map(([key, value], index) =>
                index % 2 === 0 ? (
                  <div key={key} className="explanation-item">
                    <h3>{key.replace(/_/g, ' ')}</h3>
                    <textarea value={value} readOnly style={{ width: '100%', height: '150px', resize: 'none' }} />
                  </div>
                ) : null
              )}
            </div>
            <div className="column">
              {Object.entries(results).filter(([key, _]) => key.includes('Explanation')).map(([key, value], index) =>
                index % 2 !== 0 ? (
                  <div key={key} className="explanation-item">
                    <h3>{key.replace(/_/g, ' ')}</h3>
                    <textarea value={value} readOnly style={{ width: '100%', height: '150px', resize: 'none' }} />
                  </div>
                ) : null
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
