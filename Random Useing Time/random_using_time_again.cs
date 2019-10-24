        static void Main(string[] args)
        {
            Console.WriteLine(randomz());

            static int randomz()
            { 
                // this is not 100% random this is what is called sudo random,
                // even then if this is run more than once to fast you will get duplicats.
                // but running this every now and then and it will be as good as random.

                DateTime dateTime = DateTime.Now; // get the datetime of now. (when run)
                double deciaml = (double)dateTime.TimeOfDay.TotalMilliseconds; 
					// convert that datetime to a decimal number (in total milliseconds).
                int integer = (int)dateTime.TimeOfDay.TotalMilliseconds; 
					// convert that datetime to an integer (in total milliseconds).
                double dif = ((integer / 100) - (deciaml / 100)) * 100; // do mathy stuff.
                dif = Math.Abs(dif); // remove the decimals and make it an absolute value
                int num = Convert.ToInt32(dif); // convert that absolute value to an int 32.
                return num;
            }
        }