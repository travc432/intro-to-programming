# Travis Crotteau, Ron Williams
# Formatted to PEP 8 standards as much as possible according to Pycharm
# modules
# DictReader is an object within the CSV module. It allows the programmer to read/write data in dictionary form
import csv
import sys
from csv import DictReader

# create reporting text file
# file_path = os.path.join('C:\\', 'Users', 'ronnv', 'Desktop', 'resolvedDay.csv')
# f = open(file_path, 'a+')


# main class
class TicketTracking:
    # constructor
    def __init__(self, tech='none', priority_status='none', status=''):
        self.tech = tech
        self.priority_status = priority_status
        self.status = status

    # our first function is the menu
    # this menu is the interface for selecting requested information from the CSV files
    def print_menu(self):
        print('\nMENU\n')
        print('1. Tickets opened')
        print('2. Tickets closed')
        print('3. Technician statistics')
        print('4. Review tickets by priority')
        print('5. Daily summary')
        print('Q. Quit')
        print()
        option = input("Enter an option: ")

        if option == '1':
            self.open_tickets()
            # the menu prints again after a selection has been made
            self.print_menu()
        elif option == '2':
            self.resolved()
            self.print_menu()
        elif option == '3':
            tech = input('\nWhich tech would you like stats on? ')
            try:
                self.tech_stats(tech)
            # raises an exception if technician isn't found
            except:
                print('\nThis tech wasn\'t found in the reports.')
            self.print_menu()
        # Lists reference numbers of high or low priority tickets
        elif option == '4':
            priority_status = input('What priority level do you want to know about? Enter high or low: ')
            self.priority(priority_status)
            self.print_menu()
        elif option == '5':
            self.daily_summary()
            self.print_menu()
        elif option == 'Q' or 'q':
            print("Goodbye!")
            exit()
        # reminds user to enter valid menu option if they input incorrect keystrokes or nothing at all
        else:
            print('Make sure to enter a valid option\n')
            self.print_menu()

    # our second function gives information about open tickets
    def open_tickets(self):
        try:
            filename = 'opened.csv'
            with open('opened.csv', 'r') as f:
                global open_tickets
                # a list!
                open_tickets = [row['Reference Number'] for row in DictReader(f)]
                reader = csv.reader(f)
                total = len(open_tickets)
                print('There are {} open tickets' .format(total))
                #  print('The following are the Reference numbers for all open tickets:\n{}' .format(open_tickets))
                print('The following are the Reference numbers for all open tickets:')
                print('\n'.join(str(x) for x in open_tickets))
        # if there are issues with the CSV file, this shows where to look
        except csv.Error as e:
                    sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    # our third function gives information about resolved tickets
    def resolved(self):
        try:
            filename = 'resolvedDay1.csv'
            with open('resolvedDay1.csv', 'r') as f:
                global resolved_tickets
                # a list!
                resolved_tickets = [row['Reference Number'] for row in DictReader(f)]
                reader = csv.reader(f)
                total = len(resolved_tickets)
                print('Total tickets resolved: {}' .format(total))
                print('The following are the Reference numbers for all resolved tickets:')
                print('\n'.join(str(x) for x in resolved_tickets))
        except csv.Error as e:
                    sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    # our fourth function gives information about priority tickets
    def priority(self, priority_status):
        with open('opened.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            # a dictionary!
            tickets_by_priority = {'low': [], 'high': []}
            for row in reader:
                if row['Reference Number']:
                    if priority_status == 'low':
                        if row['Priority'] == '3 - Standard (IS)':
                            tickets_by_priority['low'].append(row['Reference Number'])
                    if priority_status == 'high':
                        if row['Priority'] == '1 - Critical (IS)' or '2 - High (IS)':
                            tickets_by_priority['high'].append(row['Reference Number'])
            if priority_status == 'low':
                print('\nThe following low priority tickets were opened:')
                # print(tickets_by_priority['low'])
                print('\n'.join(str(x) for x in tickets_by_priority['low']))
            if priority_status == 'high':
                print('\nThe following high priority tickets were opened:')
                # print(tickets_by_priority['high'])
                print('\n'.join(str(x) for x in tickets_by_priority['high']))
        with open('resolvedDay1.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            # a dictionary!
            tickets_by_priority = {'low': [], 'high': []}
            for row in reader:
                if row['Reference Number']:
                    if priority_status == 'low':
                        if row['Priority'] == '3 - Standard (IS)':
                            tickets_by_priority['low'].append(row['Reference Number'])
                    if priority_status == 'high':
                        if row['Priority'] == '1 - Critical (IS)' or '2 - High (IS)':
                            tickets_by_priority['high'].append(row['Reference Number'])
        if priority_status == 'low':
            print('\nThe following low priority tickets were resolved:')
            # print(tickets_by_priority['low'])
            print('\n'.join(str(x) for x in tickets_by_priority['low']))
        if priority_status == 'high':
            print('\nThe following high priority tickets were resolved:')
            # print(tickets_by_priority['high'])
            print('\n'.join(str(x) for x in tickets_by_priority['high']))

    # our fifth function gives information about the technicians' current workload
    def tech_stats(self, tech):
        with open('resolvedDay1.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            tech_num_resolved = 0
            tech_p3 = 0
            tech_p2 = 0
            tech_p1 = 0
            for row in reader:
                if tech == row['Assigned Analyst']:
                    tech_num_resolved += 1
                    if row['Priority'] == '1 - Critical (IS)':
                        tech_p1 += 1
                    elif row['Priority'] == '2 - High (IS)':
                        tech_p2 += 1
                    else:
                        tech_p3 += 1
            if tech_num_resolved == 0:
                raise NameError()
            print('\n%s closed %d tickets.' % (tech, tech_num_resolved))
            print('\n%d were Priority 1 calls.' % tech_p1)
            print('%d were Priority 2 calls.' % tech_p2)
            print('%d were Priority 3 calls.' % tech_p3)

    # our sixth and final function gives an overview of the day's workload
    def daily_summary(self):
        # Initially this function didn't work if previous function were run.  We found that it
        # was because num_resolved and num_opened were only defined in those functions and
        # not this one, so we made sure it include the code to define them here.  No matter
        # which function will run first, the variable will be defined.
        with open('resolvedDay1.csv', 'r') as f:
            global resolved_tickets
            # a list!
            resolved_tickets = [row['Reference Number'] for row in DictReader(f)]
            num_resolved = len(resolved_tickets)
        with open('opened.csv', 'r') as f:
            global open_tickets
            # a list!
            open_tickets = [row['Reference Number'] for row in DictReader(f)]
            num_opened = len(open_tickets)
            print('%d tickets were opened.' % num_opened)
            print('%d tickets were closed.' % num_resolved)

            if num_opened > num_resolved:
                print('We fell behind by %d tickets.' % (num_opened - num_resolved))

            if num_opened < num_resolved:
                print('We caught up by %d tickets.' % (num_resolved - num_opened))

            if num_opened == num_resolved:
                print('We broke even today.')


def main():
    review_assigned = TicketTracking()
    review_assigned.print_menu()


if __name__ == "__main__":
    main()
