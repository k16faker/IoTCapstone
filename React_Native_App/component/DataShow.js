import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button} from 'react-native';

import { initializeApp } from "firebase/app";
import{ doc, getDoc, getFirestore} from "firebase/firestore";

import firestore from '@react-native-firebase/firestore';
import { useEffect, useState } from 'react';

import {
  LineChart,
  BarChart,
  PieChart,
  ProgressChart,
  ContributionGraph,
  StackedBarChart
} from "react-native-chart-kit";


const firebaseConfig = {
  apiKey: "AIzaSyAravWh0TImhLqLmtzBVVgTqFxleNx_WCI",
  authDomain: "iotcapstone-4b75d.firebaseapp.com",
  projectId: "iotcapstone-4b75d",
  storageBucket: "iotcapstone-4b75d.appspot.com",
  messagingSenderId: "949646824175",
  appId: "1:949646824175:web:c0edc7e40e8dd0bd24c11a"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const recRef = doc(db, "object_count", "current_counts");
const recRef_9 = doc(db, "object_count", "09");
const recRef_10 = doc(db, "object_count", "10");
const recRef_11 = doc(db, "object_count", "11");
const recRef_12 = doc(db, "object_count", "12");
const recRef_13 = doc(db, "object_count", "13");
const recRef_14 = doc(db, "object_count", "14");
const recRef_15 = doc(db, "object_count", "15");
const recRef_16 = doc(db, "object_count", "16");
const recRef_17 = doc(db, "object_count", "17");
const recRef_18 = doc(db, "object_count", "18");
const recRef_19 = doc(db, "object_count", "19");
const recRef_20 = doc(db, "object_count", "20");
const recRef_21 = doc(db, "object_count", "21");
const recRef_22 = doc(db, "object_count", "22");
const recRef_23 = doc(db, "object_count", "23");


const DataShow = () => {
  const [isChart, setIsChart] = useState(false);

  const changeChart = () => {
    setIsChart(!isChart);
  }


  const [numRectangles, setNumRectangles] = useState(null);
  const [numTreadmil, setNumTreadmil] = useState(null);
  const [numLag, setNumLag] = useState(null);
  const [numMachine1, setNumMachine1] = useState(null);
  const [numMachine2, setNumMachine2] = useState(null);

  const [num_9, setNum_9] = useState(null);
  const [num_10, setNum_10] = useState(null);
  const [num_11, setNum_11] = useState(null);
  const [num_12, setNum_12] = useState(null);
  const [num_13, setNum_13] = useState(null);
  const [num_14, setNum_14] = useState(null);
  const [num_15, setNum_15] = useState(null);
  const [num_16, setNum_16] = useState(null);
  const [num_17, setNum_17] = useState(null);
  const [num_18, setNum_18] = useState(null);
  const [num_19, setNum_19] = useState(null);
  const [num_20, setNum_20] = useState(null);
  const [num_21, setNum_21] = useState(null);

  


  async function getNum() {
    const docSnap = await getDoc(recRef);
    const docSnap9 = await getDoc(recRef_9);
    const docSnap10 = await getDoc(recRef_10);
    const docSnap11 = await getDoc(recRef_11);
    const docSnap12 = await getDoc(recRef_12);
    const docSnap13 = await getDoc(recRef_13);
    const docSnap14 = await getDoc(recRef_14);
    const docSnap15 = await getDoc(recRef_15);
    const docSnap16 = await getDoc(recRef_16);
    const docSnap17 = await getDoc(recRef_17);
    const docSnap18 = await getDoc(recRef_18);
    const docSnap19 = await getDoc(recRef_19);
    const docSnap20 = await getDoc(recRef_20);
    const docSnap21 = await getDoc(recRef_21);

    if (docSnap.exists()) {
      setNumRectangles(docSnap.data().num_rectangles);
      setNumTreadmil(docSnap.data().num_people_treadmil);
      setNumLag(docSnap.data().num_of_lag);
      setNumMachine1(docSnap.data().num_of_machine1);
      setNumMachine2(docSnap.data().num_of_machine2);
    }

    if(docSnap9.exists()){
      setNum_9(docSnap9.data().num_peoples/docSnap9.data().counted_number);
    }
    if(docSnap10.exists()){
      setNum_10(docSnap10.data().num_peoples/docSnap10.data().counted_number);
    }
    if(docSnap11.exists()){
      setNum_11(docSnap11.data().num_peoples/docSnap11.data().counted_number);
    }
    if(docSnap12.exists()){
      setNum_12(docSnap12.data().num_peoples/docSnap12.data().counted_number);
    }
    if(docSnap13.exists()){
      setNum_13(docSnap13.data().num_peoples/docSnap13.data().counted_number);
    }
    if(docSnap14.exists()){
      setNum_14(docSnap14.data().num_peoples/docSnap14.data().counted_number);
    }
    if(docSnap15.exists()){
      setNum_15(docSnap15.data().num_peoples/docSnap15.data().counted_number);
    }
    if(docSnap16.exists()){
      setNum_16(docSnap16.data().num_peoples/docSnap16.data().counted_number);
    }
    if(docSnap17.exists()){
      setNum_17(docSnap17.data().num_peoples/docSnap17.data().counted_number);
    }
    if(docSnap18.exists()){
      setNum_18(docSnap18.data().num_peoples/docSnap18.data().counted_number);
    }
    if(docSnap19.exists()){
      setNum_19(docSnap19.data().num_peoples/docSnap19.data().counted_number);
    }
    if(docSnap20.exists()){
      setNum_20(docSnap20.data().num_peoples/docSnap20.data().counted_number);
    }
    if(docSnap21.exists()){
      setNum_21(docSnap21.data().num_peoples/docSnap21.data().counted_number);
    }
  }

  return (
    <View style={styles.container}>
      {!isChart && <View style={styles.header}>
        <Text style={styles.header}>인원 수</Text>
      </View>}
      {isChart && <Text style={styles.header}>시간대 별 인원 수</Text>}
      {!isChart && 
      <View style={styles.content}>
        <View style={styles.row}>
          <Text style={styles.label}>전체 인원:</Text>
          <Text style={styles.value}>{numRectangles}명</Text>
        </View>
        <View style={styles.row}>
          <Text style={styles.label}>런닝머신 인원:</Text>
          <Text style={styles.value}>{numTreadmil}명</Text>
        </View>
        <View style={styles.row}>
          <Text style={styles.label}>랙 사용중 인원:</Text>
          <Text style={styles.value}>{numLag}명</Text>
        </View>
        <View style={styles.row}>
          <Text style={styles.label}>머신 1구역 인원:</Text>
          <Text style={styles.value}>{numMachine1}명</Text>
        </View>
        <View style={styles.row}>
          <Text style={styles.label}>머신 2구역 인원:</Text>
          <Text style={styles.value}>{numMachine2}명</Text>
        </View>
        <Button title="인원수 갱신" onPress={getNum} style={styles.button} />
      </View>}
      {isChart && <View>
          <LineChart
            data={{
              labels: ['09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'],
              datasets: [
                {
                  data: [
                    num_9,
                    num_10,
                    num_11,
                    num_12,
                    num_13,
                    num_14,
                    num_15,
                    num_16,
                    num_17,
                    num_18,
                    num_19,
                    num_20,
                    num_21,
                  ],
                },
              ],
            }}
            width={300}
            height={200}
            chartConfig={{
              backgroundColor: '#F6F6F6',
              backgroundGradientFrom: '#F6F6F6',
              backgroundGradientTo: '#F6F6F6',
              decimalPlaces: 0,
              color: (opacity = 1) => `rgba(0, 198, 255, ${opacity})`,
              labelColor: (opacity = 1) => `rgba(28, 28, 28, ${opacity})`,
              style: {
                borderRadius: 16,
                marginTop: 50,
              },
              propsForDots: {
                r: '6',
                strokeWidth: '2',
                stroke: '#000000',
              },
              minValue: 0,
            }}
            bezier
            style={styles.chart}
          />
        </View>}
        {isChart &&<Button title="인원수 보기" onPress={changeChart} style={styles.button} />}
        {!isChart && <Button title="통계 보기" onPress={changeChart} style={styles.button} />}
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
  },
  header: {
    backgroundColor: '#00C6FF',
    padding: 10,
    borderRadius: 10,
  },
  header:{
  color: 'black',
  fontSize: 24,
  fontWeight: 'bold',
  textAlign: 'center',
  },
  content: {
  flex: 1,
  marginTop: 20,
  padding: 10,
  backgroundColor: 'white',
  borderRadius: 10,
  },
  row:{
  flexDirection: 'row',
  alignItems: 'center',
  paddingVertical: 10,
  borderBottomColor: '#E5E5E5',
  borderBottomWidth: 1,
  },
  label: {
  flex: 1,
  fontSize: 18,
  fontWeight: 'bold',
  color: '#1C1C1C',
  },
  value:{
  flex: 1,
  fontSize: 18,
  color: '#4F4F4F',
  textAlign: 'right',
  },
  button:{
  marginTop: 20,
  backgroundColor: '#000000',
  borderRadius: 10,
  paddingVertical: 10,
  },
  buttonText: {
  color: 'white',
  fontSize: 18,
  fontWeight: 'bold',
  textAlign: 'center',
  },
  });

  export default DataShow;