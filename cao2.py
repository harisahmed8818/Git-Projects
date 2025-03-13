class WeatherReport:


    def printReport(self, city, temperature, atmosphere, date , time_stamp):
        print( '-----------------------------------------')
        print(f'|                                       |')
        print(f'|             {city}                    |')
        print(f'|                                       |')
        print(f'|             {temperature}             |')
        print(f'|                                       |')
        print(f'|             {atmosphere}              |')
        print(f'|                                       |')
        print(f'|             {date}                    |')
        print(f'|                                       |')
        print(f'|             {time_stamp}              |')
        print( '-----------------------------------------')


weather_report = WeatherReport()

weather_report.printReport('lahore', '20 Celsius', 'rainy', '11-03-2025' , '09:00 am')