#include <bits/stdc++.h>
using namespace std;

unsigned long long mergeAndCountSplitInv(vector<int> &nums, int left,
                                         int mid, int right)
{
    vector<int> temp;
    unsigned long long inversions = 0;
    int firstHalfIndexStart = left, secondHalfIndexStart = mid, k = left;

    while ((firstHalfIndexStart < mid) && (secondHalfIndexStart <= right))
    {
        if (nums[firstHalfIndexStart] < nums[secondHalfIndexStart])
        {
            temp.push_back(nums[firstHalfIndexStart]);
            ++firstHalfIndexStart;
        }
        else if (nums[secondHalfIndexStart] < nums[firstHalfIndexStart])
        {
            temp.push_back(nums[secondHalfIndexStart]);
            ++secondHalfIndexStart;
            inversions += (mid - firstHalfIndexStart);
        }
    }

    while (firstHalfIndexStart < mid)
    {
        temp.push_back(nums[firstHalfIndexStart]);
        ++firstHalfIndexStart;
    }

    while (secondHalfIndexStart <= right)
    {
        temp.push_back(nums[secondHalfIndexStart]);
        ++secondHalfIndexStart;
    }

    int i = left;
    for (int j = 0; j < temp.size(); ++j)
    {
        nums[i] = temp[j];
        i++;
    }

    // cout << "sorted array" << endl;
    // for (int i = 0; i < nums.size(); ++i)
    // {
    //     cout << nums[i] << " ";
    // }
    // cout << endl;

    return inversions;
}

unsigned long long sortAndCount(vector<int> &nums, int left, int right) // hacer el vector modificable
{

    unsigned long long inversions = 0;

    // if has to be here
    if (right > left)
    {
        int mid = (right + left) / 2;
        inversions = sortAndCount(nums, left, mid);
        inversions += sortAndCount(nums, mid + 1, right);
        inversions += mergeAndCountSplitInv(nums, left, mid + 1, right);
    }

    return inversions;
    // cout << "suma: " << firstHalf.size() + secondHalf.size() << endl;
}

// cambiar inversions por unsigned long long
int main()
{
    int num;
    vector<int> nums;
    freopen("IntegerArray.txt", "r", stdin);
    while (cin >> num)
    {
        nums.push_back(num);
    }
    unsigned long long ans = sortAndCount(nums, 0, nums.size() - 1);
    cout << "inversions are: " << ans << endl;
    return 0;
}