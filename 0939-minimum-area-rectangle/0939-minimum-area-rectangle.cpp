class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        
        unordered_map<int, vector<int>> xgroup;
        unordered_map<int, vector<int>> ygroup;
        unordered_set<long long> st;

        for (auto &p : points) {
            int x = p[0], y = p[1];
            xgroup[x].push_back(y);
            ygroup[y].push_back(x);
            st.insert(((long long)x << 32) | y);
        }

        int ans = INT_MAX;

        for (auto &col : xgroup) {
            int x = col.first;
            auto &ys = col.second;

            for (int i = 0; i < ys.size(); i++) {
                for (int j = i + 1; j < ys.size(); j++) {

                    int y1 = ys[i];
                    int y2 = ys[j];

                    for (int xp : ygroup[y1]) {

                        if (xp == x) continue;

                        long long key = ((long long)xp << 32) | y2;

                        if (st.count(key)) {
                            int area = abs(x - xp) * abs(y1 - y2);
                            ans = min(ans, area);
                        }
                    }
                }
            }
        }

        return ans == INT_MAX ? 0 : ans;
    }
};