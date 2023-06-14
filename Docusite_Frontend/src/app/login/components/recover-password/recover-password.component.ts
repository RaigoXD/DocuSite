import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-recover-password',
  templateUrl: './recover-password.component.html',
  styleUrls: ['./recover-password.component.scss']
})
export class RecoverPasswordComponent implements OnInit {

  recoverForm!: FormGroup;
  errorMessage!: string;
  constructor(
    public formBuilder: FormBuilder
  ) {}
  
  buildForm(): FormGroup {
    return this.formBuilder.group({
      email: ['', Validators.email],
    });
  }

  ngOnInit(): void {
    this.recoverForm = this.buildForm();
  }

  emailValidation(){
    if(this.recoverForm.get('email')?.hasError('email')){
      this.errorMessage = 'Email invalido'
      return true
    }
    return false
  }

  onSubmit(){
    const validation = this.emailValidation()
    if(this.recoverForm.value.email && !validation){
      return;
    }
    return;
  }

}
