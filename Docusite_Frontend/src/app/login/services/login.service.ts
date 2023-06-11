import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { UserReceive, UserSend } from '../interfaces/user.interface';
import { Observable } from 'rxjs';
import { StorageService } from 'src/app/core/services/storage/storage.service';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  url = 'http://localhost:5000/api/v1/login/'
  constructor(public httpClient: HttpClient,public storage: StorageService) { }

  loginUser(userLogin: UserSend): Observable<UserReceive>{
    const logged = this.httpClient.post<UserReceive>(this.url, userLogin);

    logged.subscribe((response) => {
      if(response){
        if(response.access != ''){
          this.storage.save('AUTH_TOKEN',response.access);
          return;
        }
      }
    });

    return logged
  }

}
