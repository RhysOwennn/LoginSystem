import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AuthService { 
  constructor() { 
  } 

  getUserDetails() { 
      return localStorage.getItem('userInfo') ? JSON.parse(localStorage.getItem('userInfo') as any) : null; 
  } 
   
  setDataInLocalStorage(variableName: any, data: any) {  // need to figure out types here
      localStorage.setItem(variableName, data); 
  } 

  getToken() { 
      return localStorage.getItem('token'); 
  } 

  clearStorage() { 
      localStorage.clear(); 
  } 
}