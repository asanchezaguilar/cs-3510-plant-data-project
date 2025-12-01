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
                            "[2] Find all the main statistics of an Attribute\n"
                            "[3] Make a Graph\n"
                            "[4] Average an Attribute by Health Status\n"
                            "[0] Exit Program\n"))

            if option == "1":  # Print plants
                system.print_plants()
            
            elif option == "2":  # Attribute statistics
                option2 = "-1"
                while option2 != "0":
                    option2 = input(("Choose an attribute to find statistics for:\n"
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

                    def show_stats(attribute_name, display_name):
                        count, mean, median, stdev, minimum, maximum = system.summarize_attribute(attribute_name)
                        print(f"\n{display_name} statistics:")
                        print(f"Count: {count}")
                        print(f"Mean: {mean}")
                        print(f"Median: {median}")
                        print(f"Standard Deviation: {stdev}")
                        print(f"Minimum: {minimum}")
                        print(f"Maximum: {maximum}\n")

                    if option2 == "1":
                        show_stats("soil_moisture", "Soil Moisture")
                        option2 = "0"
                    elif option2 == "2":
                        show_stats("ambient_temperature", "Ambient Temperature")
                        option2 = "0"
                    elif option2 == "3":
                        show_stats("soil_temperature", "Soil Temperature")
                        option2 = "0"
                    elif option2 == "4":
                        show_stats("humidity", "Humidity")
                        option2 = "0"
                    elif option2 == "5":
                        show_stats("light_intensity", "Light Intensity")
                        option2 = "0"
                    elif option2 == "6":
                        show_stats("soil_ph", "Soil pH")
                        option2 = "0"
                    elif option2 == "7":
                        show_stats("nitrogen_level", "Nitrogen Level")
                        option2 = "0"
                    elif option2 == "8":
                        show_stats("phosphorus_level", "Phosphorus Level")
                        option2 = "0"
                    elif option2 == "9":
                        show_stats("potassium_level", "Potassium Level")
                        option2 = "0"
                    elif option2 == "10":
                        show_stats("chlorophyll_content", "Chlorophyll Content")
                        option2 = "0"
                    elif option2 == "11":
                        show_stats("electrochemical_signal", "Electrochemical Signal")
                        option2 = "0"
                    elif option2 == "0":
                        break
                    else:
                        print("Invalid option. Please try again.")

            elif option == "3":  # Graphing
                option2 = "-1"
                while option2 != "0":
                    option2 = input(("[1] Graph an Attribute over Time\n"
                                     "[2] Correlation Graph Between Two Attributes\n"
                                     "[0] Go Back\n"))

                    if option2 == "1":
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
                                elif option4 == "2":
                                    system.attribute_over_time("ambient_temperature", plant_id)
                                elif option4 == "3":
                                    system.attribute_over_time("soil_temperature", plant_id)
                                elif option4 == "4":
                                    system.attribute_over_time("humidity", plant_id)
                                elif option4 == "5":
                                    system.attribute_over_time("light_intensity", plant_id)
                                elif option4 == "6":
                                    system.attribute_over_time("soil_ph", plant_id)
                                elif option4 == "7":
                                    system.attribute_over_time("nitrogen_level", plant_id)
                                elif option4 == "8":
                                    system.attribute_over_time("phosphorus_level", plant_id)
                                elif option4 == "9":
                                    system.attribute_over_time("potassium_level", plant_id)
                                elif option4 == "10":
                                    system.attribute_over_time("chlorophyll_content", plant_id)
                                elif option4 == "11":
                                    system.attribute_over_time("electrochemical_signal", plant_id)
                                else:
                                    print("Invalid option. Please try again.")

                                option4 = option3 = option2 = "0"

                    elif option2 == "2":
                        attr_map = {
                            "1": "soil_moisture",
                            "2": "ambient_temperature",
                            "3": "soil_temperature",
                            "4": "humidity",
                            "5": "light_intensity",
                            "6": "soil_ph",
                            "7": "nitrogen_level",
                            "8": "phosphorus_level",
                            "9": "potassium_level",
                            "10": "chlorophyll_content",
                            "11": "electrochemical_signal"
                        }

                        first = "-1"
                        while first != "0":
                            first = input(("Choose the first attribute (x-axis):\n"
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

                            if first == "0":
                                break
                            if first not in attr_map:
                                print("Invalid option. Please try again.")
                                continue

                            attr1 = attr_map[first]

                            second = "-1"
                            while second != "0":
                                second = input(("Choose the second attribute (y-axis):\n"
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

                                if second == "0":
                                    break
                                if second not in attr_map:
                                    print("Invalid option. Please try again.")
                                    continue

                                attr2 = attr_map[second]

                                system.correlation_graph(attr1, attr2)
                                second = first = option2 = "0"

                    elif option2 == "0":
                        break
                    else:
                        print("Invalid option. Please try again.")

            elif option == "4":  # Average by health status
                option2 = "-1"
                while option2 != "0":
                    option2 = input(("Choose an attribute to average by health status:\n"
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

                    def show_by_health(attribute_name, display_name):
                        results = system.average_by_health_status(attribute_name)
                        print(f"\nAverage {display_name} by health status:")
                        for status in results:
                            print(f"{status}: {results[status]}")
                        print()

                    if option2 == "1":
                        show_by_health("soil_moisture", "Soil Moisture")
                        option2 = "0"
                    elif option2 == "2":
                        show_by_health("ambient_temperature", "Ambient Temperature")
                        option2 = "0"
                    elif option2 == "3":
                        show_by_health("soil_temperature", "Soil Temperature")
                        option2 = "0"
                    elif option2 == "4":
                        show_by_health("humidity", "Humidity")
                        option2 = "0"
                    elif option2 == "5":
                        show_by_health("light_intensity", "Light Intensity")
                        option2 = "0"
                    elif option2 == "6":
                        show_by_health("soil_ph", "Soil pH")
                        option2 = "0"
                    elif option2 == "7":
                        show_by_health("nitrogen_level", "Nitrogen Level")
                        option2 = "0"
                    elif option2 == "8":
                        show_by_health("phosphorus_level", "Phosphorus Level")
                        option2 = "0"
                    elif option2 == "9":
                        show_by_health("potassium_level", "Potassium Level")
                        option2 = "0"
                    elif option2 == "10":
                        show_by_health("chlorophyll_content", "Chlorophyll Content")
                        option2 = "0"
                    elif option2 == "11":
                        show_by_health("electrochemical_signal", "Electrochemical Signal")
                        option2 = "0"
                    elif option2 == "0":
                        break
                    else:
                        print("Invalid option. Please try again.")

            elif option == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")
