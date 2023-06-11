import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class StorageService {
  private storage: Storage;
  constructor() {
    this.storage = localStorage;
   }

   public save(key: string, value: any) {
    value = JSON.stringify(value);
    this.storage.setItem(key, value);
  }

  public read(key: string): any {
    const value = this.storage.getItem(key);
    return value ? JSON.parse(value) : null;
  }

  public remove(key: string) {
    return this.storage.removeItem(key);
  }

  public clear() {
    this.storage.clear();
  }
}
