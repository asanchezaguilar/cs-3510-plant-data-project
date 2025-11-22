from system import PlantIRS

class Interface():
    @staticmethod
    def start():
        system = PlantIRS()
        system.load_data()
        print("***********************************************************")
        print("*Welcome to the Plant Data Retrieval System*")
        print("***********************************************************")
        
        option = "-1"
        while option != "0":
            option = input(("What would you like to do?\n"
                            "[1] Print all Plants\n"
                            "[2] Find the average of an Attribute\n"
                            "[3] Make a Graph\n"
                            "[0] Exit Program\n"))

            if option == "1":
                system.print_plants()
            
            elif option == "2":
                option2 = "-1"
                while option2 != "0":
                    option2 = input(("Choose an attribute to take the average of:\n"
                                     "[1] - Soil Moisture\n"
                                     "[2] - Ambient Temperature\n"
                                     "[3] - Soil Temperature\n"
                                     "[4] - Humidity\n"
                                     "[5] - Light Intensity\n"
                                     "[6] - Soil pH\n"
                                     "[7] - Nitrogen Level\n"
                                     "[8] - Phosphorus Level\n"
                                     "[9] - Potassium Level\n"
                                     "[10] - Chlorophyll Content\n"
                                     "[11] - Electrochemical Signal\n"
                                     "[0] - Go Back\n"))
                    if option2 == "1":
                        avg = system.average("soil_moisture")
                        print(f"\nSoil Moisture average: {avg}\n")
                        option2 = "0"
                    elif option2 == "2":
                        avg = system.average("ambient_temperature")
                        print(f"\nAmbient Temperature average: {avg}\n")
                        option2 = "0"
                    elif option2 == "3":
                        avg = system.average("soil_temperature")
                        print(f"\nSoil Temperature average: {avg}\n")
                        option2 = "0"
                    elif option2 == "4":
                        avg = system.average("humidity")
                        print(f"\nHumidity average: {avg}\n")
                        option2 = "0"
                    elif option2 == "5":
                        avg = system.average("light_intensity")
                        print(f"\nLight Intensity average: {avg}\n")
                        option2 = "0"
                    elif option2 == "6":
                        avg = system.average("soil_ph")
                        print(f"\nSoil pH average: {avg}\n")
                        option2 = "0"
                    elif option2 == "7":
                        avg = system.average("nitrogen_level")
                        print(f"\nNitrogen Level average: {avg}\n")
                        option2 = "0"
                    elif option2 == "8":
                        avg = system.average("phosphorus_level")
                        print(f"\nPhosphorus Level average: {avg}\n")
                        option2 = "0"
                    elif option2 == "9":
                        avg = system.average("potassium_level")
                        print(f"\nPotassium Level average: {avg}\n")
                        option2 = "0"
                    elif option2 == "10":
                        avg = system.average("chlorophyll_content")
                        print(f"\nChlorophyll Content average: {avg}\n")
                        option2 = "0"
                    elif option2 == "11":
                        avg = system.average("electrochemical_signal")
                        print(f"\nElectrochemical Signal average: {avg}\n")
                        option2 = "0"
                    elif option2 == "0":
                        break
                    else:
                        print("Invalid option. Please try again.")

            elif option == "3":
                option2 = "-1"
                while option2 != "0":
                    option2 = input(("[1] Graph an Attribute over Time\n[2] Placeholder\n[0] Go Back\n"))
                    if option2 == "1":
                        # Choose plant
                        option3 = "-1"
                        while option3 != "0":
                            option3 = input(("What Plant would you like to graph?\n"
                                             "[1] - Plant 1\n"
                                             "[2] - Plant 2\n"
                                             "[3] - Plant 3\n"
                                             "[4] - Plant 4\n"
                                             "[5] - Plant 5\n"
                                             "[6] - Plant 6\n"
                                             "[7] - Plant 7\n"
                                             "[8] - Plant 8\n"
                                             "[9] - Plant 9\n"
                                             "[10] - Plant 10\n"
                                             "[0] - Go Back\n"))
                            if option3 == "0":
                                break
                            if not option3.isdigit():
                                print("Invalid option. Please try again.")
                                continue
                            plant_id = int(option3)

                            # Choose attribute
                            option4 = "-1"
                            while option4 != "0":
                                option4 = input(("What attribute would you like to graph?\n"
                                                 "[1] - Soil Moisture\n"
                                                 "[2] - Ambient Temperature\n"
                                                 "[3] - Soil Temperature\n"
                                                 "[4] - Humidity\n"
                                                 "[5] - Light Intensity\n"
                                                 "[6] - Soil pH\n"
                                                 "[7] - Nitrogen Level\n"
                                                 "[8] - Phosphorus Level\n"
                                                 "[9] - Potassium Level\n"
                                                 "[10] - Chlorophyll Content\n"
                                                 "[11] - Electrochemical Signal\n"
                                                 "[0] - Go Back\n"))

                                if option4 == "0":
                                    break
                                elif option4 == "1":
                                    system.attribute_over_time("soil_moisture", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "2":
                                    system.attribute_over_time("ambient_temperature", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "3":
                                    system.attribute_over_time("soil_temperature", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "4":
                                    system.attribute_over_time("humidity", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "5":
                                    system.attribute_over_time("light_intensity", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "6":
                                    system.attribute_over_time("soil_ph", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "7":
                                    system.attribute_over_time("nitrogen_level", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "8":
                                    system.attribute_over_time("phosphorus_level", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "9":
                                    system.attribute_over_time("potassium_level", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "10":
                                    system.attribute_over_time("chlorophyll_content", plant_id)
                                    option4 = option3 = option2 = "0"
                                elif option4 == "11":
                                    system.attribute_over_time("electrochemical_signal", plant_id)
                                    option4 = option3 = option2 = "0"
                                else:
                                    print("Invalid option. Please try again.")
                    elif option2 == "2":
                        print("Feature coming soon.")
                    elif option2 == "0":
                        break
                    else:
                        print("Invalid option. Please try again.")

            elif option == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")
