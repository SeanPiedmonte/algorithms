import java.util.*;

// This should get the right solution some of the time.
public class EightQueensProblem {
    public final static int N = 8;

    public int[] queens;
    private int[] consByRow = new int[8];

    public EightQueensProblem() {
        queens = new int[N];
        for(int i=0; i<N; i++) {
            int col = (int)(Math.random()*N);
            queens[i] = col;
        }
    }

    public void printBoard() {
        for(int row=0; row<N; row++) {
            for(int col=0; col<N; col++) {
                char c = (queens[row] == col ? 'Q' : ' ');
                if(col == N-1)
                    System.out.println(c);
                else
                    System.out.print(c + " | ");
            }

            if(row < N-1) {
                for(int i = 0; i < (N*4)-2; i++) {
                    System.out.print("-");
                }
                System.out.println();
            }
        }
    }

    public int conflicts(int row, int col) {
        int conflicts = 0;
        for(int i=0; i<N; i++) {
            if (i != row) {
                    if(queens[i]==col) {
                        conflicts++;
                    }
                    else if(Math.abs(i-row) == Math.abs(queens[i] - col)) {
                        conflicts++;
                    }
            }
        }
        return conflicts;
    }

    public boolean isSolved() {
        boolean solved = true;
        for(int row=0; row<N; row++) {
            if(conflicts(row, queens[row]) > 0) {
                solved = false;
                break;
            }
        }
        return solved;
    }

    public int pickRandomQueen() {
        int newIndex = (int)(Math.random()*N);
        return queens[newIndex];
    }

    // Almost never completes the problem
    public void minConflicts() {
        int minAttacks, pickedQueen, minConPos, newNumCons;
        int[] positions;
        while(!isSolved()) {
            minAttacks = N + 1;
            pickedQueen = pickRandomQueen();
            minConPos = -1;
            for (int i = 0; i < N; i++) {
                queens[i] = pickedQueen;
                newNumCons = conflicts(i, queens[i]);
                if(newNumCons < minAttacks) {
                    minConPos = queens[i];
                    minAttacks = newNumCons;
                }
                queens[i] = pickedQueen;
            }

            queens[pickedQueen] = minConPos;

        }
    }
    public static void main(String args[]) {
        EightQueensProblem pro = new EightQueensProblem();
        pro.printBoard();
    }
}
