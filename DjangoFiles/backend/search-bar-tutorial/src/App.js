/* 
import './App.css';
// Allowed extensions for input file
// https://blog.logrocket.com/create-search-bar-react-from-scratch/
// search bar tutorial ^
// export default function CSVReader() {
//   const papaConfig = {
//     Papa.parse(csvFile, {
//       download: true,
//       complete: function (input) {
//            const records = input.data;
//       })
  
//     }
// }
function csvToArray(str, delimiter = ",") {
  const headers = str.slice(0, str.indexOf("\n")).split(delimiter);
  
  // slice from \n index + 1 to the end of the text
  // use split to create an array of each csv value row
  const rows = str.slice(str.indexOf("\n") + 1).split("\n");
  const arr = rows.map(function (row) {
    const values = row.split(delimiter);
    const el = headers.reduce(function (object, header, index) {
      object[header] = values[index];
      return object;
    }, {});
    return el;
  });

  // return the array
  return arr;
}
function App() {
  
  const reader = new FileReader();
  reader.readAsText("DjangoFiles/backend/treecover_loss_by_region__ha.csv");

  reader.onload = function (e) {
    const text = e.target.result;
    const data = csvToArray(text);

    data.map((post) => (
      <div key={post.iso}>
        <p>{post.iso}</p>
        <p>{post.Year}</p>
      </div>
    ));
  };
  return (
    <div className="App">
      <div className = "Content">
        <h1>Hello there</h1>
      </div>
    </div>
  );
}

export default App; */