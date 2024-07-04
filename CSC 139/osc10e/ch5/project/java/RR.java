import java.util.*;//Imports ArrayList, which is used to store the tasks in the scheduling queue.

public class RR implements Algorithm {//RR class implements the Algorithm interface and its methods.

    private List<Task> queue;//We declare a private List instance variable called queue that represents the queue of tasks to be executed.
    private int quantum;//The time quantum used for the RR algorithm.
    /*
    public RR(List<Task> queue, int quantum) {
        this.queue = queue;
        this.quantum = quantum;
    }
    */
    public RR(List<Task> queue) {//The SJF constructor takes in a list of tasks.
        this.queue = queue;//Initializes the queue instance variable with the passed list of tasks.
        this.quantum = 10;//We are assuming that the length of a time quantum is 10 milliseconds.
    }

    // Invokes the scheduler
    public void schedule(){
        // loop through tasks in ready queue and execute them
        while (!queue.isEmpty()) {//While the queue is not empty.
            Task currentTask = pickNextTask();//pickNextTask() picks the next task from the queue based on the RR algorithm.
            int slice = Math.min(currentTask.getBurst(), quantum);//Calculates the time slice that a task should be allowed to run for in a Round Robin scheduling algorithm.
            CPU.run(currentTask, slice);//Simulates the execution of the current task for the time slice specified by the quantum variable.
            currentTask.setBurst(currentTask.getBurst() - slice);//Updates the remaining burst time of the current task after executing it.

            if (currentTask.getBurst() > 0) {//It the task still has some burst time left.
                queue.add(currentTask);//Add it back to the queue for further executing.
            }
        }
    }

    // Selects the next task using the appropriate scheduling algorithm
    public Task pickNextTask(){
        if(queue.isEmpty()) {//If the queue is empty.
            return null;//Return null.
        }
        return queue.remove(0);//Removes and returns the first task from the queue list.
    }

}