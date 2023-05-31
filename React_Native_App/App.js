// import { StatusBar } from 'expo-status-bar';
// import { StyleSheet, Text, View } from 'react-native';

// import { initializeApp } from "firebase/app";
// import{ doc, getDoc, getFirestore} from "firebase/firestore";

// import firestore from '@react-native-firebase/firestore';
// import { useEffect, useState } from 'react';


// const firebaseConfig = {
//   apiKey: "AIzaSyAravWh0TImhLqLmtzBVVgTqFxleNx_WCI",
//   authDomain: "iotcapstone-4b75d.firebaseapp.com",
//   projectId: "iotcapstone-4b75d",
//   storageBucket: "iotcapstone-4b75d.appspot.com",
//   messagingSenderId: "949646824175",
//   appId: "1:949646824175:web:c0edc7e40e8dd0bd24c11a"
// };

// const app = initializeApp(firebaseConfig);
// const db = getFirestore(app);

// const recRef = doc(db, "object_count", "current_counts");


// export default function App() {
//   const [numRectangles, setNumRectangles] = useState(null);

//   useEffect(() => {
//     async function getNumRectangles() {
//       const docSnap = await getDoc(recRef);
//       if (docSnap.exists()) {
//         setNumRectangles(docSnap.data().num_rectangles);
//       }
//     }
//     getNumRectangles();
//   }, []);

//   if (numRectangles === null) {
//     return <Text>Loading...</Text>;
//   }

//   return (
//     <View style={[styles.view]} >
//       <Text style={{alignItems:'center'}}>
//       현재 인원수: {numRectangles}
//       </Text>
//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
//   view: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   }
// });






// import { StatusBar } from 'expo-status-bar';
// import { StyleSheet, Text, View, Button} from 'react-native';

// import { initializeApp } from "firebase/app";
// import{ doc, getDoc, getFirestore} from "firebase/firestore";

// import firestore from '@react-native-firebase/firestore';
// import { useEffect, useState } from 'react';


// const firebaseConfig = {
//   apiKey: "AIzaSyAravWh0TImhLqLmtzBVVgTqFxleNx_WCI",
//   authDomain: "iotcapstone-4b75d.firebaseapp.com",
//   projectId: "iotcapstone-4b75d",
//   storageBucket: "iotcapstone-4b75d.appspot.com",
//   messagingSenderId: "949646824175",
//   appId: "1:949646824175:web:c0edc7e40e8dd0bd24c11a"
// };

// const app = initializeApp(firebaseConfig);
// const db = getFirestore(app);

// const recRef = doc(db, "object_count", "current_counts");


// export default function App() {
//   const [numRectangles, setNumRectangles] = useState(null);
//   const [numTreadmil, setNumTreadmil] = useState(null);

//   async function getNum() {
//     const docSnap = await getDoc(recRef);
//     if (docSnap.exists()) {
//       setNumRectangles(docSnap.data().num_rectangles);
//       setNumTreadmil(docSnap.data().num_people_treadmil);
//     }
//   }



//   return (
//     <View style={[styles.view]} >
//       <Text style={{alignItems:'center'}}>
//       현재 총 인원수: {numRectangles}
//       {"\n"}
//       현재 트레드밀 인원수: {numTreadmil}
//       </Text>
//       <Button title="인원수 갱신" onPress={getNum} />
//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   },
//   view: {
//     flex: 1,
//     backgroundColor: '#fff',
//     alignItems: 'center',
//     justifyContent: 'center',
//   }
// });


import { StyleSheet, Text, View, Button} from 'react-native';
import { useEffect, useState } from 'react';
import DataShow from './component/DataShow';



const App = () => {


  const [isChecked, setIsChecked] = useState(false);

  return (
    <View style={styles.container}>
      {!isChecked && <Text style={{fontSize: 30, fontWeight: 'bold', marginBottom: 30, textAlign: 'center'}}>헬스장 선택</Text>}
      {!isChecked && <Button title="A 헬스장" onPress={() => setIsChecked(true)} style={styles.checkbutton} />}
      {!isChecked && <Button title="B 헬스장" onPress={() => setIsChecked(true)} style={styles.checkbutton} />}
      {!isChecked && <Button title="C 헬스장" onPress={() => setIsChecked(true)} style={styles.checkbutton} />}
      {isChecked && <DataShow />}
      {isChecked && <Button title="헬스장 선택" onPress={() => setIsChecked(false)} />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F6F6F6',
    alignItems: 'stretch',
    justifyContent: 'flex-start',
    padding: 20,
    marginTop: 30,
  },
  checkbutton: {
    marginTop: 1000,
  }
  });


export default App;
