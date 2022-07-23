import axios from 'axios';

import { API_BASEURL, getAccessToken, getAxiosConfig } from '../config';

const access_token = getAccessToken()

const axiosInstance = axios.create({
  baseURL: API_BASEURL,
  headers:getAxiosConfig(access_token).headers
});

export default axiosInstance;
