import axiosInstance from '../api/axios';

const Get = axiosInstance.get;
const Post = axiosInstance.post;
const Put = axiosInstance.put;
const Delete = axiosInstance.delete;
const Patch = axiosInstance.patch;

export { Get, Post, Patch, Put, Delete };
