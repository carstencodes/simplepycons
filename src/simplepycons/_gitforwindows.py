#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class GitForWindowsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gitforwindows"

    @property
    def original_file_name(self) -> "str":
        return "gitforwindows.svg"

    @property
    def title(self) -> "str":
        return "Git for Windows"

    @property
    def primary_color(self) -> "str":
        return "#80B3FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Git for Windows</title>
     <path d="M11.976.0003a1.541 1.541 0 0 0-1.0928.4526L8.707
 2.6287l2.7604 2.7604c.6417-.2166 1.377-.0715
 1.8882.4399.514.5145.6583 1.2563.4362 1.9l.9101.9102
 3.2768-3.2764L13.0684.4529A1.5394 1.5394 0 0 0 11.976.0003ZM7.638
 3.698 5.926 5.4101l4.9095
 4.9095c.1535.1536.332.267.5217.3423V8.831a1.8198 1.8198 0 0
 1-.6024-.4011c-.5441-.5437-.6749-1.3422-.3958-2.0104Zm10.916
 2.24-3.2765 3.2764 1.1743 1.1747c.6436-.2217 1.3862-.0782
 1.9001.4366.7185.7183.7185 1.8823 0
 2.6008-.7186.7187-1.8823.7187-2.6012
 0-.5402-.5407-.674-1.3344-.4003-2l-1.1427-1.1423-.588.588c-.6036.604-.6036
 1.5829 0 2.1865l4.9935 4.993 4.9342-4.9342c.6035-.6038.6035-1.5829
 0-2.1865zM5.34 5.9956.4528 10.8825c-.6037.604-.6037 1.5828 0
 2.1864l4.8395 4.8396 4.8873-4.8873c.6035-.6038.6035-1.5828
 0-2.1865zm7.5293
 2.9497v1.4986c.0516-.04.1048-.077.1522-.1243l.611-.611zm-1.5121
 4.2224c-.2317.072-.4514.1927-.6349.376-1.6323 1.6325-3.2647
 3.2649-4.8971 4.8972l5.1065 5.1062c.6033.6035 1.582.6035 2.1861
 0l4.8967-4.8968-5.1065-5.1065c-.012-.012-.0264-.0202-.0387-.0317v1.9618a1.854
 1.854 0 0 1 .4863.3477c.7183.7182.7183 1.8819 0
 2.6012-.7185.7182-1.883.7182-2.6008 0-.7184-.7193-.7184-1.883
 0-2.6012a1.8406 1.8406 0 0 1 .6024-.4012z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/git-for-windows/git-for-wi
ndows.github.io/blob/db9a134ed0fd484568124c1f79cb011eddb9a21d/img/gwin'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
