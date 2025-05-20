# ----> WORK IN PROGRESS <----
# A script that makes various calculations for flight preparations.


start_bold = "\033[1m"
end_bold = "\033[0;0m"

while True:
    "\n"
    print()
    print(
        "-- FLIGHT CALC - Choose a subject from the list below --\n"
        "\n"
        "   FLIGHT PERFORMANCE (F)\n"  # --->
        "   MASS AND BALANCE (MB)\n"
        "   FLIGHT PLANNING (FP)\n"
        "   OPERATIONAL PROCEDURES (O)\n"
        "   METEOROLOGY (M)\n")
    choice = input("Choose a subject : ").lower()
    print()


    def climb_gradient():
        while True:
            try:
                print('1. Calculating ground gradient from air gradient (get air gradient from AFM).')
                air_gradient = float(input("enter air gradient (%) : "))
                TAS = int(input("enter TAS (kts) : "))
                HW = int(input("enter head wind (kts) : "))
#                print("---> !Skipping data input!")
                GS = TAS - HW
                wind_factor = TAS/GS
                print()
                ground_gradient = air_gradient*wind_factor
                print(f"{start_bold}GROUND GRADIENT = {ground_gradient:.1f}%{end_bold}")
                print()
                print("2. Calculating distance travelled over the ground from ground gradient.")
                print("Class B aircraft : screen height = 50ft.")
                screen_height = 50
                alt_to_climb_to = int(input("Enter altitude (AGL) to climb to (ft): "))
                alt_to_cover = alt_to_climb_to-screen_height
                ground_distance = (alt_to_cover/ground_gradient)*100
                print(f"{start_bold}GROUND DISTANCE TRAVELLED = {ground_distance:,.0f}ft or {ground_distance*0.3048:,.0f}m{end_bold}")
                print()
                print("3. Calculating obstacle clearance\n"
                "screen height class A = 11m; class B = 15m")
                print()
                scr_height = int(input("Enter screen height in meter: "))
                obstacle_height = int(input("Enter obstacle height in meter : "))
                obstacle_distance_from_TODA = int(input("Enter distance obstacle from TODA in meter : "))
                distance_obstcle_times_gradient = obstacle_distance_from_TODA*(ground_gradient/100)
                height_to_cover = scr_height+distance_obstcle_times_gradient
                obstacle_clearance = height_to_cover-obstacle_height
                print(f"{start_bold}Obstacle will be cleared by {obstacle_clearance:,.0f}m.{end_bold}")
            except ValueError:
                print("---> ! Please enter an integer!")                
                print()
                print()


    def density_altitude():
        print(
            "--- DENSITY ALTITUDE ---\n" \
            "Density altitude differs from pressure altitude with\n"
            f"{start_bold}120ft per °C from standard temperature.  Convert to \n"
            f"pressure altitude if no flight level.{end_bold}\n")
        print()
        fl_input = int(input("Enter flight level, ex : '50' : "))
        fl_altitude = fl_input*100
        temp = int(input("Enter outside t° : "))
        std_temp_at_alt = 15-(2*(fl_input//10))
        temp_difference = temp-std_temp_at_alt

        DA = fl_altitude+(120*(temp-std_temp_at_alt))
        print(f"{start_bold}DENSITY ALTITUDE = {DA:,.0f}ft{end_bold}.")
        print()
        print()

    def rate_of_climb():
        ias = int(input("Enter speed IAS in kts : "))
        altitude = int(input("Enter pressure altitude in feet : "))
        TAS = ias*(1+(altitude/1000*.02))
        print(f"{TAS:.0f}")





    if choice == "f": # print subcats flight performance :
        print("--- SUBJECT : FLIGHT PERFORMANCE ---\n"
            "   Climb Gradient (CG)\n"  # -->
            "   Density Altitude (DA)\n"
            "   Rate of Climb (RC)\n"
            "   Rate of Descent (RD)\n"
            "   Glide Slope Height (GlS)\n"
            "   Take-off/field length requirements (TO) - CLASS B\n"
            "   Landing/field length requirements (LA) - CLASS B\n"
            "   Runway Slope (RS)\n"
        )
        print()
        choice_f = input("Choose a category : ").lower()
        print()
        if choice_f == 'cg':
            climb_gradient()
        elif choice_f == 'da':
            density_altitude()
        elif choice_f == 'rc':
            rate_of_climb()
        elif choice_f == 'rd':
            rate_of_descent()
        elif choice_f == 'gls':
            glide_slope_height()        
        elif choice_f == 'to':
            take-off()
        elif choice_f == ''
