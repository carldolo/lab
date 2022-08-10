class Television:
    '''
    Class which controls TV functionalities
    '''
    MIN_CHANNEL: int = 0     # Minimum TV channel
    MAX_CHANNEL: int = 3     # Maximum TV channel

    MIN_VOLUME: int = 0      # Minimum TV volume
    MAX_VOLUME: int = 2      # Maximum TV volume


    
    def __init__(self) -> None:
        '''
        Initialization method which populates the class with default values
        '''
        self.__tv_channel = Television.MIN_CHANNEL
        self.__tv_volume = Television.MIN_VOLUME
        self.__tv_status = False

    def power(self) -> None:
        '''
        Method to toggle TV on or off.
        '''
        if self.__tv_status == False:
            self.__tv_status = True
        else:
            self.__tv_status = False

    def channel_up(self) -> None:
        '''
        Method to increment TV channel.
        '''
        if self.__tv_status == True:
            if self.__tv_channel == Television.MAX_CHANNEL:
                self.__tv_channel = Television.MIN_CHANNEL
            else:
                self.__tv_channel += 1
        else:
            pass

    def channel_down(self) -> None:
        '''
        Method to decrement TV channel.
        '''
        if self.__tv_status == True:
            if self.__tv_channel == Television.MIN_CHANNEL:
                self.__tv_channel = Television.MAX_CHANNEL
            else:
                self.__tv_channel -= 1
        else:
            pass

    def volume_up(self) -> None:
        '''
        Method to increment TV volume.
        '''
        if self.__tv_status == True:
            if self.__tv_volume == Television.MAX_VOLUME:
                pass
            else:
                self.__tv_volume += 1
        else:
            pass

    def volume_down(self) -> None:
        '''
        Method to decrement TV volume.
        '''
        if self.__tv_status == True:
            if self.__tv_volume == Television.MIN_VOLUME:
                pass
            else:
                self.__tv_volume -= 1
        else:
            pass

    def __str__(self) -> str:
        '''
        Method to return status of TV power, TV channel, and TV volume.
        :return: String describing tv power status, channel and volume level.
        '''
        if self.__tv_status == True:
            return f'TV status: Is on = True, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}'
        else:
            return f'TV status: Is on = False, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}'
