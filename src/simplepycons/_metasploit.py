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


class MetasploitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "metasploit"

    @property
    def original_file_name(self) -> "str":
        return "metasploit.svg"

    @property
    def title(self) -> "str":
        return "Metasploit"

    @property
    def primary_color(self) -> "str":
        return "#2596CD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Metasploit</title>
     <path d="M11.353 0h1.368q4.19.218 8.144
 1.616.217.077.216.309-.015 4.033-.002 12.102 0 .81-.093
 1.173c-.217.845-.76 1.635-1.326 2.325q-.318.388-1.024 1.046-2.955
 2.75-6.01
 5.094-.183.14-.516.335h-.17q-.627-.42-.945-.673-3.992-3.184-5.442-4.459-1.348-1.185-2.169-2.611c-.369-.64-.466-1.287-.465-2.099q.01-6.048.002-12.218c0-.183.09-.264.261-.325Q7.145.227
 11.352 0ZM7.474 7.864q0-.094.069-.031l2.797 2.516a.374.372 21.2 0 1
 .122.276l-.006 4.333a.182.182 0 0 0 .183.184l2.524-.018a.11.11 89.8 0
 0 .108-.11q-.007-2.201.01-4.461.002-.173.146-.29 1.397-1.145
 2.946-2.393.068-.055.068.032v10.881q0 .092.063.024.794-.865
 1.628-1.838.71-.83.984-1.87.26-.989.262-1.997.007-4.754.009-9.768a.136.136
 0 0 0-.137-.136q-1.15.004-2.424 0c-.287-.002-.441-.022-.619.149Q14.16
 5.317 11.982 7.4a.046.046 0 0 1-.062 0Q9.782 5.437 7.769
 3.525c-.234-.222-.515-.381-.843-.373q-1.09.026-2.33.005-.184-.004-.184.18-.003
 4.54.005 9.032.002.536.036 1.027c.076 1.093.2 2.126.803 3.021.574.852
 1.329 1.656 2.126 2.405q.023.022.054.026.04.006.04-.034z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/rapid7/metasploit-framewor
k/blob/f8bd7dfd834354c9a2e2c03e1d9f5d53f8881954/docs/assets/images/fav'''

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
