import React, { useState } from 'react';

function App() {
  const [count, setCount] = useState(0);
  
  // Linting Issue 1: Unused variable
  const unusedVariable = 10;

  // Linting Issue 2: Inline style object creation
  const increment = () => {
    setCount(count + 1);
  };

  // Linting Issue 3: Improper JSX structure (missing key attribute in a list)
  const items = ['Item 1', 'Item 2', 'Item 3'];

  return (
    <div className="App">
      <h1>Hello, React!</h1>
      <button onClick={increment}>Increment Count</button>
      <p>Count: {count}</p>

      <div>
        {items.map((item) => (
          <div>{item}</div> // Missing key prop here
        ))}
      </div>

      {/* Linting Issue 4: Unnecessary div */}
      <div>
        <span>Redundant container div</span>
      </div>
    </div>
  );
}

export default App;

