
import java.util.*;//Imports ArrayList, which is used to store the tasks in the scheduling queue.

public class PriorityRR implements Algorithm {//PriorityRR class implements the Algorithm interface and its methods.
    
    private List<Task> queue;//We declare a private List instance variable called queue that represents the queue of tasks to be executed.
    private int quantum;//The time quantum used for the RR algorithm.
    private int time;//Time is used to keep track of the total time taken to execute all the tasks in the queue.
    
    public PriorityRR(List<Task> queue) {//The PriorityRR constructor takes in a list of tasks.
        this.queue = queue;//Initializes the queue instance variable with the passed list of tasks.
        this.quantum = 10;//The time quantum used for the RR algorithm.
        this.time = 0;//Time is set to 0 in the constructor.
    }

    public void schedule() {
        List<Task> completedTasks = new ArrayList<>();//Initializes a new ArrayList of Task objects named completedTasks.
        //^The purpose of this list is to store tasks that have completed their execution or tasks whose burst time has become zero.
        while (!queue.isEmpty()) {//While the queue is not empty.
            Task currentTask = pickNextTask();//pickNextTask() picks the next task from the queue based on the PriorityRR algorithm.
            if (currentTask == null) {//If null, it means that no task can be picked for execution in this time quantum.
                time++;//Time is incremented by 1.
                continue;//Loop moves on to next iteration using 'continue' statement.
            }
            int burst = Math.min(currentTask.getBurst(), quantum);//Calculates the time slice or burst time for the current task that will be run on the CPU.
            //CPU.run(currentTask, currentTask.getBurst());
            currentTask.setBurst(currentTask.getBurst() - burst);//Reduces the burst time of the current task by the minimum of its remaining burst time and the quantum value. 
            time += burst;//Adds burst to time.
            if (currentTask.getBurst() == 0) {//If remaining burst is 0.
                completedTasks.add(currentTask);//Add task to list of completed tasks.
                System.out.println("Task " + currentTask.getName() + " finished.\n");//Tell user that task is finished.
            } else {//Else...
                queue.add(currentTask);//Add the task back to the queue.
                CPU.run(currentTask, currentTask.getBurst());//Simulates the execution of a task on a CPU.
            }
        }
        //for (Task task : completedTasks) {
            //System.out.println("Task " + task.getName() + " finished.");
        //}
    }

    public Task pickNextTask() {
        Task nextTask = null;//Sets next task to null.
        int maxPriority = Integer.MIN_VALUE;//Sets min value to find max.
        for (Task task : queue) {//For each task in the queue.
            if (task.getPriority() > maxPriority && task.getBurst() > 0) {//Checks if the priority of the current task is higher than the maximum priority found so far and if the burst time of the task is greater than zero.
                maxPriority = task.getPriority();//Sets new highest priority value.
                nextTask = task;//Sets the task.
            }
        }
        if (nextTask != null) {//If the next task is not null.
            queue.remove(nextTask);//Remove the next task from the queue.
            return nextTask;//Return the next task.
        }
        // No tasks with positive burst time found, now search for tasks with zero burst time
        for (Task task : queue) {//For each task in the queue.
            if (task.getBurst() == 0) {//If the task burst is 0.
                queue.remove(task);//Remove the task from the queue.
                return task;//Return the task.
            }
        }
        return null;
    }
}

/*
import java.util.*;//Imports ArrayList, which is used to store the tasks in the scheduling queue.

public class PriorityRR implements Algorithm {//PriorityRR class implements the Algorithm interface and its methods.
    
    private List<Task> queue;//We declare a private List instance variable called queue that represents the queue of tasks to be executed.
    private int quantum;//The time quantum used for the RR algorithm.
    private int time;//Time is used to keep track of the total time taken to execute all the tasks in the queue.
    
    public PriorityRR(List<Task> queue) {//The PriorityRR constructor takes in a list of tasks.
        this.queue = queue;//Initializes the queue instance variable with the passed list of tasks.
        this.quantum = 10;//The time quantum used for the RR algorithm.
        this.time = 0;//Time is set to 0 in the constructor.
    }

    public void schedule() {
        List<Task> completedTasks = new ArrayList<>();//Initializes a new ArrayList of Task objects named completedTasks.
        //^The purpose of this list is to store tasks that have completed their execution or tasks whose burst time has become zero.
        while (!queue.isEmpty()) {//While the queue is not empty.
            Task currentTask = pickNextTask();//pickNextTask() picks the next task from the queue based on the PriorityRR algorithm.
            if (currentTask == null) {//If null, it means that no task can be picked for execution in this time quantum.
                time++;//Time is incremented by 1.
                continue;//Loop moves on to next iteration using 'continue' statement.
            }
            int burst = Math.min(currentTask.getBurst(), quantum);//Calculates the time slice or burst time for the current task that will be run on the CPU.
            //CPU.run(currentTask, currentTask.getBurst());
            currentTask.setBurst(currentTask.getBurst() - burst);//Reduces the burst time of the current task by the minimum of its remaining burst time and the quantum value. 
            time += burst;//Adds burst to time.
            if (currentTask.getBurst() == 0) {//If remaining burst is 0.
                completedTasks.add(currentTask);//Add task to list of completed tasks.
                System.out.println("Task " + currentTask.getName() + " finished.\n");//Tell user that task is finished.
            } else {//Else...
                queue.add(currentTask);//Add the task back to the queue.
                CPU.run(currentTask, currentTask.getBurst());//Simulates the execution of a task on a CPU.
            }
        }
        //for (Task task : completedTasks) {
            //System.out.println("Task " + task.getName() + " finished.");
        //}
    }

    public Task pickNextTask() {
        Task nextTask = null;//Sets next task to null.
        int minPriority = Integer.MAX_VALUE;//Sets max value to find min.
        for (Task task : queue) {//For each task in the queue.
            if (task.getPriority() < minPriority && task.getBurst() > 0) {//Checks if the priority of the current task is lower than the minimum priority found so far and if the burst time of the task is greater than zero. 
                minPriority = task.getPriority();//Sets new lowest priority value.
                nextTask = task;//Sets the task.
            }
        }
        if (nextTask != null) {//If the next task is not null.
            queue.remove(nextTask);//Remove the next task from the queue.
            return nextTask;//Return the next task.
        }
        // No tasks with positive burst time found, now search for tasks with zero burst time
        for (Task task : queue) {//For each task in the queue.
            if (task.getBurst() == 0) {//If the task has a burst time of 0.
                queue.remove(task);//Remove the task from the queue.
                return task;//Return the task.
            }
        }
        return null;
    }
}
*/