export interface UserReceive {
    refresh: string;
    access: string;
    user: {
        uuid: string;
        rol: {
            code: string;
            description: string;
        }
        username: string;
        email: string;
        first_name: string;
        last_name: string;
        is_active: boolean;
    }
}

export interface UserSend {
    username: string;
    password: string;
}