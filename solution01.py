class AirConditioning:
    '''
    A class representing an air conditioning system.

    Attributes
    ----------
    __status (bool): The status of the air conditioner (True if on, False if off).
    __temperature (int): The current temperature setting of the air conditioner.
    '''


    __status = False
    __temperature = None

    @property
    def status(self):
        return AirConditioning.__status
    
    @status.setter
    def status(self, new_status):
        None

    @property
    def temperature(self):
        if AirConditioning.__status:
            return AirConditioning.__temperature

    
    @temperature.setter
    def temperature(self, new_temperature):
        None

    @classmethod
    def switch_on(cls):
        '''
        Switches on the air conditioner and sets the temperature to 18.
        '''
        if cls.__status == False:
            cls.__status = True
            cls.__temperature = 18

    @classmethod
    def switch_off(cls):
        '''
        Switches off the air conditioner and sets the temperature to None.
        '''
        if cls.__status == True:
            cls.__status = False
            cls.__temperature = None
        else:
            print('Кондиционер уже выключен.')

    @classmethod
    def reset(cls):
        '''
        Resets the temperature to 18 if the air conditioner is on.
        '''
        if cls.__status:
            cls.__temperature = 18

    @classmethod
    def get_temperature(cls):
        '''
        Returns the current temperature setting.
        '''
        return cls.__temperature
    
    @classmethod
    def raise_temperature(cls):
        '''
        Increases the temperature by 1, if the air conditioner is on and the temperature is less than 43.
        '''
        if cls.__status:
            if cls.__temperature < 43:
                cls.__temperature += 1
    
    @classmethod
    def lower_temperature(cls):
        '''
        Decreases the temperature by 1, if the air conditioner is on and the temperature is more than 0.
        '''
        if cls.__status:
            if cls.__temperature > 0:
                cls.__temperature -= 1

    def __repr__(self):
        if AirConditioning.__status:
            return f'Кондиционер включен. Температурный режим: {AirConditioning.__temperature} градусов.'
        else:
            return 'Кондиционер выключен.'
