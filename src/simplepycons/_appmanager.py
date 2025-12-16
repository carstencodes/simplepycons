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


class AppmanagerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appmanager"

    @property
    def original_file_name(self) -> "str":
        return "appmanager.svg"

    @property
    def title(self) -> "str":
        return "AppManager"

    @property
    def primary_color(self) -> "str":
        return "#DCAF74"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AppManager</title>
     <path d="M11.783.249c-.075 0-.142.038-.197.127-.208 1.515-.182
 1.451-.53 3.616-.045.35-.244 1.257-.36 1.806-.109.55-.372 1.312-.561
 2.06q-.27 1.106-.77 2.47a43 43 0 0 1-1.148 2.81q-.648 1.43-1.66
 3.078a31 31 0 0 1-2.201 3.146q-.54.675-1.122 1.27c-.966 1.008-1.647
 1.624-3.131 2.88-.536.573 1.167-.066 1.53-.24.842-.402.99-.493
 1.71-.986.668-.514 1.292-1.123 1.593-1.411q.5-.473
 1.567-1.783c1.611-.8 5.132-1.44 6.994-1.387 2.984.076 4.214.741 5.137
 2.548.207.468.458 1.004.683 1.5q.35.743.838 1.363.5.635.931.635.42 0
 1.148-.419.73-.405
 1.283-.904c.378-.324.483-.515.483-.668q0-.067-.04-.094-.028-.027-.095-.014a.6.6
 0 0 0-.122.014c-.045.009-.01-.026-.064-.008a.6.6 0 0 1-.122.013q-.648
 0-1.66-1.58-1-1.593-2.12-4.078a356 356 0 0
 1-2.215-5.077c-.729-1.728-1.557-3.372-2.313-5.029q-1.134-2.484-1.876-3.605c-.366-.562-1.131-2.049-1.59-2.053zm.916
 6.615c-.007.122.825 1.594 2.149 4.612q2.025 4.618 2.025
 4.767l-.027.014q-.04 0-.405-.068a11.6 11.6 0 0 0-2.336-.243q-3.173
 0-6.414 1.58 1.093-1.485 1.998-3.133.918-1.647
 1.432-2.93.526-1.283.877-2.363.365-1.08.514-1.661c.093-.335.173-.537.187-.575"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/muntashirakon/AppManager/b'''

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
