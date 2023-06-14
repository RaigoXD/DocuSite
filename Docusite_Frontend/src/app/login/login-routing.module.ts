import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RecoverPasswordComponent } from './components/recover-password/recover-password.component';
import { CreateAccountComponent } from './components/create-account/create-account.component';

export const loginRoutes: Routes = [
  {
    path: 'recover',
    component: RecoverPasswordComponent
  },
  {
    path: 'create',
    component: CreateAccountComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(loginRoutes)],
  exports: [RouterModule]
})
export class LoginRoutingModule { }
