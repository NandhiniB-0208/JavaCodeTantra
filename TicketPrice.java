package q10847;

public class TicketPrice {
    int INFANT_AGE = 3;
    int CHILD_AGE = 13;
    int SENIOR_CITIZEN_AGE = 60;
    int CENTENARIAN_AGE = 100;

    public void printTicketPrice(int age) {
        if (age <= INFANT_AGE || age >= CENTENARIAN_AGE) {
            System.out.println("Ticket Price: 0");
        } else if (age >= SENIOR_CITIZEN_AGE) {
            System.out.println("Ticket Price: 5");
        } else {
            System.out.println("Ticket Price: 10");
        }
    }
}