import axios from 'axios';

const instance = axios.create({
  baseURL: 'https://692eb84a7af2e99d.mokky.dev', 
  timeout: 1000, 
  headers: { 'Content-Type': 'application/json' }
});

export default instance;