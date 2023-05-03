
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = Arrays.stream(nums1).boxed().collect(Collectors.toSet());
        Set<Integer> set2 =  Arrays.stream(nums2).boxed().collect(Collectors.toSet());
        Set<Integer> intersection = new HashSet<>(set1);
        intersection.retainAll(set2);
        set1.removeAll(intersection);
        set2.removeAll(intersection);
        List<Integer> dif1 = new ArrayList<>(set1);
        List<Integer> dif2 = new ArrayList<>(set2);
        List<List<Integer>> answer = new ArrayList<>();
        answer.add(dif1);
        answer.add(dif2);
        return answer;
    }
}