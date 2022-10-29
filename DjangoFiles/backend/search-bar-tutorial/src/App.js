
import './App.css';
import Papa from "papaparse";
import CSVFile from 'treecover_loss_by_region__ha.csv'

// Allowed extensions for input file
const allowedExtensions = ["csv"];

function App() {
  return (
    <div className="App">
      Papa.parse(CSVFile, config)
      <input placeholder="Enter Post Title"/>
    </div>
  );
}

export default App;
