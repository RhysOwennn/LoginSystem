import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  form: FormGroup;

  constructor(
    private _api : ApiService, 
    private _auth: AuthService, 
    private router: Router, 
    public fb: FormBuilder 
    
  ) {
    this.form = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  ngOnInit(): void {
  }

  login() { 
    let formInformation = this.form.value 
    console.log(formInformation) 
    this._api.postTypeRequest('login', formInformation).subscribe((res: any) => {   // need to figure out types here
      console.log(res) 
      if(res.access_token){ 
        this._auth.setDataInLocalStorage('token', res.access_token) 
        this.router.navigate(['profile']) 
      } 
    }, (err: any) => { 
      console.log(err) 
    }); 
  } 
}