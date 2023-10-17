import { formatDistance } from "date-fns";
import { useCallback, useEffect, useState } from "react";
import { Pagination, Spinner, Userpic } from "../../../components";
import { usePage, usePageSize } from "../../../components/Pagination/Pagination";
import { Block, Elem } from "../../../utils/bem";
import { isDefined } from "../../../utils/helpers";
import './PeopleList.styl';
import { CopyableTooltip } from '../../../components/CopyableTooltip/CopyableTooltip';

export const PeopleList = ({ usersList, onSelect, selectedUser, totalItems, fetchUsers, defaultSelected }) => {
  const [currentPage] = usePage('page', 1);
  const [currentPageSize] = usePageSize('page_size', 30);

  const selectUser = useCallback((user) => {
    if (selectedUser?.id === user.id) {
      onSelect?.(null);
    } else {
      onSelect?.(user);
    }
  }, [selectedUser]);

  useEffect(() => {
    fetchUsers(currentPage, currentPageSize);
  }, []);

  useEffect(() => {
    if (isDefined(defaultSelected) && usersList) {
      const selected = usersList.find(({ user }) => user.id === Number(defaultSelected));

      if (selected) selectUser(selected.user);
    }
  }, [usersList, defaultSelected]);

  return (
    <>
      <Block name="people-list">
        <Elem name="wrapper">

          {usersList ? (
            <Elem name="users">
              <Elem name="header">
                <Elem name="column" mix="avatar"/>
                <Elem name="column" mix="email">Email</Elem>
                <Elem name="column" mix="name">Name</Elem>
                <Elem name="column" mix="last-activity">Last Activity</Elem>
              </Elem>
              <Elem name="body">
                {usersList.map(({ user }) => {
                  const active = user.id === selectedUser?.id;

                  return (
                    <Elem key={`user-${user.id}`} name="user" mod={{ active }} onClick={() => selectUser(user)}>
                      <Elem name="field" mix="avatar">
                        <CopyableTooltip title={'User ID: ' + user.id} textForCopy={user.id}>
                          <Userpic user={user} style={{ width: 28, height: 28 }}/>
                        </CopyableTooltip>
                      </Elem>
                      <Elem name="field" mix="email">
                        {user.email}
                      </Elem>
                      <Elem name="field" mix="name">
                        {user.first_name} {user.last_name}
                      </Elem>
                      <Elem name="field" mix="last-activity">
                        {formatDistance(new Date(user.last_activity), new Date(), { addSuffix: true })}
                      </Elem>
                    </Elem>
                  );
                })}
              </Elem>
            </Elem>
          ) : (
            <Elem name="loading">
              <Spinner size={36}/>
            </Elem>
          )}
        </Elem>
        <Pagination
          page={currentPage}
          urlParamName="page"
          totalItems={totalItems}
          pageSize={currentPageSize}
          pageSizeOptions={[30, 50, 100]}
          onPageLoad={fetchUsers}
          style={{ paddingTop: 16 }}
        />
      </Block>
    </>
  );
};
