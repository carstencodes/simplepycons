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


class VIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "v"

    @property
    def original_file_name(self) -> "str":
        return "v.svg"

    @property
    def title(self) -> "str":
        return "V"

    @property
    def primary_color(self) -> "str":
        return "#5D87BF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>V</title>
     <path d="M15.583
 23.4965c.0673.1924-.0435.3484-.2472.3484h-6.262c-.4075
 0-.8502-.3113-.9881-.6947L.0426.7837C-.105.3925.149.1152.5276.1599l6.393.6158c.4056.0391.8441.383.9787.7675l7.6837
 21.9533zM23.4736.1599l-6.393.6159c-.4055.0391-.8436.3832-.9775.7678l-3.8275
 10.9895 3.6784
 10.5098L23.9586.7837c.1378-.3834-.0795-.663-.485-.6238z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/vlang/v-logo/blob/eec050c9'''

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
