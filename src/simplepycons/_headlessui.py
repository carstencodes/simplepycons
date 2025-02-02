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


class HeadlessUiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "headlessui"

    @property
    def original_file_name(self) -> "str":
        return "headlessui.svg"

    @property
    def title(self) -> "str":
        return "Headless UI"

    @property
    def primary_color(self) -> "str":
        return "#66E3FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Headless UI</title>
     <path d="M4.477
 13.192c-.36-2.274-.584-3.711-.65-4.805-.062-1.035.051-1.354.1-1.468.169-.395.424-.746.746-1.029.093-.081.363-.288
 1.366-.548 1.06-.275 2.496-.507 4.769-.867 2.274-.36 3.71-.584
 4.804-.65 1.034-.062 1.354.051 1.468.1.395.169.746.424
 1.029.747.08.093.287.362.547 1.366.242.933.45 2.156.743 3.987l-14.646
 4.89c-.085-.515-.176-1.085-.276-1.723Zm-3.762.596C.018 9.387-.33
 7.187.425 5.422a6.665 6.665 0 0 1 1.743-2.401C3.614 1.757 5.813 1.41
 10.211.713c4.4-.698 6.6-1.046 8.367-.291.92.393 1.74.99 2.399 1.743
 1.264 1.447 1.612 3.647 2.308 8.047.697 4.4 1.045 6.601.29
 8.366a6.664 6.664 0 0 1-1.743 2.402c-1.445 1.263-3.645 1.611-8.045
 2.308-4.398.697-6.598 1.045-8.363.29a6.666 6.666 0 0
 1-2.4-1.743c-1.263-1.448-1.611-3.648-2.308-8.048H.715v.001Zm7.759
 7.814c1.178-.072 2.695-.31 4.94-.665 2.247-.356 3.762-.599 4.905-.895
 1.107-.288 1.617-.568 1.947-.856a4.286 4.286 0 0 0
 1.12-1.543c.172-.402.281-.974.212-2.116-.071-1.178-.309-2.696-.665-4.942-.355-2.247-.598-3.763-.894-4.906-.287-1.107-.568-1.618-.855-1.947a4.285
 4.285 0 0
 0-1.543-1.12c-.402-.174-.974-.282-2.116-.213-1.178.071-2.694.309-4.94.664-2.246.357-3.762.6-4.905.896-1.107.287-1.616.568-1.946.855a4.286
 4.286 0 0 0-1.12 1.543c-.173.403-.281.974-.212 2.116.07 1.179.308
 2.696.664 4.943.356 2.246.598 3.762.895 4.905.287 1.108.567 1.618.855
 1.947.423.485.95.868 1.543 1.121.402.173.973.282 2.116.213Z" />
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
