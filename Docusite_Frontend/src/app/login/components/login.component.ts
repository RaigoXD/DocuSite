import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Subscription } from 'rxjs';
import { LoginService } from '../services/login.service';
import { UserReceive } from '../interfaces/user.interface';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  hide = true;
  userInfo!: UserReceive;
  subscription$!: Subscription[];
  logInForm!: FormGroup;
  constructor(
    public formBuilder: FormBuilder,
    private loginService: LoginService
  ) {}
  
  buildForm(): FormGroup {
    return this.formBuilder.group({
      username: ['', [Validators.required, Validators.maxLength(30)]],
      password: ['', [Validators.required, Validators.maxLength(30)]],
    });
  }



  ngOnInit(): void {
    this.logInForm = this.buildForm();
  }

  onSubmit() {
    if (this.logInForm.invalid) {
      window.alert('Datos inválidos');
      return;
    }
  
    try {
      this.loginService.loginUser(this.logInForm.value).subscribe(
        (data: UserReceive) => {
          this.userInfo = data;
          console.log(this.userInfo);          
        },
        (error) => {
          console.error(error);
        }
      );
    } catch (error) {
      console.error(error);
    }
  }

}
