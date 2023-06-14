import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LoginRoutingModule } from './login-routing.module';
import { LoginComponent } from './components/login.component';
import { MaterialModule } from '../shared/material.module';
import { CreateAccountComponent } from './components/create-account/create-account.component';
import { RecoverPasswordComponent } from './components/recover-password/recover-password.component';


@NgModule({
  declarations: [
    LoginComponent,
    CreateAccountComponent,
    RecoverPasswordComponent
  ],
  imports: [
    CommonModule,
    LoginRoutingModule,
    MaterialModule
  ]
})
export class LoginModule { }
