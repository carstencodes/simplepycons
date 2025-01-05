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


class WritedotasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "writedotas"

    @property
    def original_file_name(self) -> "str":
        return "writedotas.svg"

    @property
    def title(self) -> "str":
        return "Write.as"

    @property
    def primary_color(self) -> "str":
        return "#5AC4EE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Write.as</title>
     <path d="M12.812 5.139l2.179 7.509a168.085 168.085 0 01.666
 2.459h.025c.054-.372.145-.772.273-1.204l.353-1.176
 1.05-3.442.213-.671c.062-.199.126-.382.192-.551.068-.167.131-.327.194-.478.062-.151.132-.301.213-.451v-.028l-1.569.105V5.139h5.169V6.88c-.364
 0-.682.119-.956.358a3.608 3.608 0 00-.711.85 6.325 6.325 0
 00-.493.984 22.78 22.78 0 00-.286.758l-3.096 8.997h-2.884L11.47
 13.02c-.053-.142-.12-.345-.199-.606a46.941 46.941 0
 01-.247-.85c-.083-.307-.173-.623-.265-.95-.092-.328-.179-.638-.259-.931h-.026c-.053.381-.14.809-.26
 1.283-.119.474-.243.937-.372 1.388-.128.451-.248.859-.358
 1.223-.111.364-.194.62-.246.771l-1.501 4.479h-2.7L1.742 9.392a27.83
 27.83 0 01-.472-1.39 3.995 3.995 0 01-.113-.418l-.094-.425L0
 7.212V5.139h6.526V6.88c-.382.027-.65.141-.806.345-.155.204-.231.466-.231.784-.009.151.001.311.032.478a4.9
 4.9 0 00.128.519l.916 3.322c.107.399.21.818.312
 1.256.101.438.184.884.247 1.336h.026l.134-.598a39.977 39.977 0
 01.331-1.429c.072-.278.155-.587.254-.922l1.993-6.832h2.95zM24
 16.628a2.232 2.232 0 11-4.464 0 2.232 2.232 0 114.464 0" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
