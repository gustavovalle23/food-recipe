import { PassportStrategy } from '@nestjs/passport';
import { Injectable } from '@nestjs/common';
import { Strategy } from 'passport-local';
import { AuthGuardType } from '@libs/constants';
import { UserEntity } from '@modules/user/domain/entities/user.entity';
import { ValidateUserQuery } from '@modules/user/commands/validate-user/validate-user.query';
import { CommandBus } from '@nestjs/cqrs';

@Injectable()
export class LocalAuthStrategy extends PassportStrategy(Strategy, AuthGuardType.Local) {

  constructor(private readonly commandBus: CommandBus) {
    super({
      usernameField: 'email',
      // The local passport strategy requires a password field but we do not need one.
      // Set the password to email so that validate is correctly called.
      // Otherwise the request would have to contain a password.
      passwordField: 'email',
    });
  }

  async validate(email: string): Promise<UserEntity> {
    const result = await this.commandBus.execute(new ValidateUserQuery({ email }));
    return result.unwrap();
  }

}
